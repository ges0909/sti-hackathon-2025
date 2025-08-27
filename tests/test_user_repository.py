import pytest
import pytest_asyncio
from unittest.mock import patch
from database import user_repository
from database.models.base import Base
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession

# Use an in-memory SQLite database for testing
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"


@pytest_asyncio.fixture(scope="function")
async def async_db_session():
    """
    Test fixture to set up an in-memory database for each test function.
    It creates all tables, yields a session, and drops all tables afterwards.
    """
    engine = create_async_engine(TEST_DATABASE_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async_session_local = async_sessionmaker(bind=engine, expire_on_commit=False)

    async with async_session_local() as session:
        yield session

    # The in-memory database is automatically discarded when the connection is closed.
    await engine.dispose()


@pytest.mark.asyncio
async def test_add_and_get_user(async_db_session):
    """Test adding a user and retrieving them by last name."""
    await user_repository.add_user(
        async_db_session,
        first_name="John",
        last_name="Doe",
        email="test@example.com",
        age=30,
    )

    user = await user_repository.get_user_by_last_name(async_db_session, "Doe")
    assert user is not None
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "test@example.com"


@pytest.mark.asyncio
async def test_delete_user_by_last_name_success(async_db_session: AsyncSession):
    """Test deleting an existing user by last name."""
    # Add test user
    await user_repository.add_user(
        async_db_session, "John", "Smith", "test@example.com", 25
    )

    # Verify user exists
    user = await user_repository.get_user_by_last_name(async_db_session, "Smith")
    assert user is not None

    # Delete user
    deleted = await user_repository.delete_user_by_last_name(async_db_session, "Smith")
    assert deleted is True

    # Verify user is gone
    user = await user_repository.get_user_by_last_name(async_db_session, "Smith")
    assert user is None


@pytest.mark.asyncio
async def test_delete_user_by_last_name_not_found(async_db_session: AsyncSession):
    """Test deleting a non-existing user by last name."""
    # Try to delete non-existing user
    deleted = await user_repository.delete_user_by_last_name(
        async_db_session, "NonExistent"
    )
    assert deleted is False


@pytest.mark.asyncio
async def test_delete_all_users(async_db_session):
    """Test deleting all users from the database."""
    # Add some users first
    await user_repository.add_user(
        async_db_session,
        first_name="Alice",
        last_name="Johnson",
        email="delete1@example.com",
        age=40,
    )
    await user_repository.add_user(
        async_db_session,
        first_name="Bob",
        last_name="Wilson",
        email="delete2@example.com",
        age=50,
    )

    # Verify they were added
    users_before_delete = await user_repository.get_all_users(async_db_session)
    assert len(users_before_delete) == 2

    # Perform the deletion
    deleted_count = await user_repository.delete_all_users(async_db_session)
    assert deleted_count == 2

    # Verify the database is empty
    users_after_delete = await user_repository.get_all_users(async_db_session)
    assert len(users_after_delete) == 0


@pytest.mark.asyncio
async def test_add_user_duplicate_email(async_db_session):
    """Test adding user with duplicate email raises ValueError."""
    await user_repository.add_user(
        async_db_session, "John", "Doe", "test@example.com", 30
    )
    
    with pytest.raises(ValueError, match="Email already exists"):
        await user_repository.add_user(
            async_db_session, "Jane", "Smith", "test@example.com", 25
        )


@pytest.mark.asyncio
async def test_get_user_by_last_name_not_found(async_db_session):
    """Test getting user by last name when not found."""
    user = await user_repository.get_user_by_last_name(async_db_session, "NotFound")
    assert user is None


@pytest.mark.asyncio
async def test_delete_all_users_empty_database(async_db_session):
    """Test deleting all users from empty database."""
    deleted_count = await user_repository.delete_all_users(async_db_session)
    assert deleted_count == 0
