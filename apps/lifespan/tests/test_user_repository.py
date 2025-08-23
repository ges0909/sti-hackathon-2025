import pytest
import pytest_asyncio
from database import user_repository
from database.models.base import Base
from database.user_repository import add_user, delete_user_by_name, get_user_by_name
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
    """Test adding a user and retrieving them by name."""
    await user_repository.add_user(
        async_db_session, name="test_user", email="test@example.com", age=30
    )

    user = await user_repository.get_user_by_name(async_db_session, "test_user")
    assert user is not None
    assert user.name == "test_user"
    assert user.email == "test@example.com"


@pytest.mark.asyncio
async def test_delete_user_by_name_success(async_db_session: AsyncSession):
    """Test deleting an existing user by name."""
    # Add test user
    await add_user(async_db_session, "test_user", "test@example.com", 25)

    # Verify user exists
    user = await get_user_by_name(async_db_session, "test_user")
    assert user is not None

    # Delete user
    deleted = await delete_user_by_name(async_db_session, "test_user")
    assert deleted is True

    # Verify user is gone
    user = await get_user_by_name(async_db_session, "test_user")
    assert user is None


@pytest.mark.asyncio
async def test_delete_user_by_name_not_found(async_db_session: AsyncSession):
    """Test deleting a non-existing user by name."""
    # Try to delete non-existing user
    deleted = await delete_user_by_name(async_db_session, "nonexistent_user")
    assert deleted is False


@pytest.mark.asyncio
async def test_delete_all_users(async_db_session):
    """Test deleting all users from the database."""
    # Add some users first
    await user_repository.add_user(
        async_db_session, name="user_to_delete1", email="delete1@example.com", age=40
    )
    await user_repository.add_user(
        async_db_session, name="user_to_delete2", email="delete2@example.com", age=50
    )

    # Verify they were added
    users_before_delete = await user_repository.get_all_users(async_db_session)
    assert len(users_before_delete) == 2

    # Perform the deletion
    await user_repository.delete_all_users(async_db_session)

    # Verify the database is empty
    users_after_delete = await user_repository.get_all_users(async_db_session)
    assert len(users_after_delete) == 0
