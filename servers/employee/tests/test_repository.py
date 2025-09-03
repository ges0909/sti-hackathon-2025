import pytest
import pytest_asyncio
from repositories.repository import Repository
from models import Base, User
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"


class UserRepositoryForTesting(Repository):
    def __init__(self):
        super().__init__(User)


@pytest_asyncio.fixture(scope="function")
async def async_db_session():
    engine = create_async_engine(TEST_DATABASE_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async_session_local = async_sessionmaker(bind=engine, expire_on_commit=False)

    async with async_session_local() as session:
        yield session

    await engine.dispose()


@pytest.mark.asyncio
async def test_repository_get_all(async_db_session):
    """Test BaseRepository get_all method."""
    repo = UserRepositoryForTesting()

    # Initially empty
    users = await repo.get_all(async_db_session)
    assert len(users) == 0

    # Add a user
    user = User(first_name="Test", last_name="User", email="test@example.com", age=25)
    await repo.add(async_db_session, user)

    # Should have one user
    users = await repo.get_all(async_db_session)
    assert len(users) == 1


@pytest.mark.asyncio
async def test_base_repository_get_by_id(async_db_session):
    """Test BaseRepository get_by_id method."""
    repo = UserRepositoryForTesting()

    # Add a user
    user = User(first_name="Test", last_name="User", email="test@example.com", age=25)
    await repo.add(async_db_session, user)

    # Get all users to find the ID
    users = await repo.get_all(async_db_session)
    user_id = users[0].id

    # Get by ID
    found_user = await repo.get_by_id(async_db_session, user_id)
    assert found_user is not None
    assert found_user.first_name == "Test"


@pytest.mark.asyncio
async def test_base_repository_delete_by_id(async_db_session):
    """Test BaseRepository delete_by_id method."""
    repo = UserRepositoryForTesting()

    # Add a user
    user = User(first_name="Delete", last_name="Me", email="delete@example.com", age=30)
    await repo.add(async_db_session, user)

    # Get the ID
    users = await repo.get_all(async_db_session)
    user_id = users[0].id

    # Delete by ID
    deleted = await repo.delete_by_id(async_db_session, user_id)
    assert deleted is True

    # Verify deletion
    found_user = await repo.get_by_id(async_db_session, user_id)
    assert found_user is None


@pytest.mark.asyncio
async def test_base_repository_delete_all(async_db_session):
    """Test BaseRepository delete_all method."""
    repo = UserRepositoryForTesting()

    # Add multiple users
    user1 = User(first_name="User", last_name="One", email="user1@example.com", age=25)
    user2 = User(first_name="User", last_name="Two", email="user2@example.com", age=30)
    await repo.add(async_db_session, user1)
    await repo.add(async_db_session, user2)

    # Verify they exist
    users = await repo.get_all(async_db_session)
    assert len(users) == 2

    # Delete all
    deleted_count = await repo.delete_all(async_db_session)
    assert deleted_count == 2

    # Verify empty
    users = await repo.get_all(async_db_session)
    assert len(users) == 0
