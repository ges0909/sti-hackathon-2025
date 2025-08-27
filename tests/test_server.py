import pytest
import pytest_asyncio
from unittest.mock import AsyncMock, MagicMock, patch
from database.models.base import Base
from database.models.user import User
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from mcp.server.session import ServerSession
from server import (
    AppContext,
    find_all_users,
    find_user_by_last_name,
    add_user,
    delete_user_by_last_name,
    delete_all_users,
    get_database_stats,
    analyze_user_prompt,
)
from schemas import UserDto

TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"


@pytest_asyncio.fixture(scope="function")
async def async_db_session():
    """Test fixture for in-memory database."""
    engine = create_async_engine(TEST_DATABASE_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async_session_local = async_sessionmaker(bind=engine, expire_on_commit=False)
    async with async_session_local() as session:
        yield session
    await engine.dispose()


@pytest_asyncio.fixture
async def mock_context(async_db_session):
    """Mock MCP context with database session."""
    mock_db = MagicMock()
    mock_db.get_async_session.return_value.__aenter__.return_value = async_db_session

    app_context = AppContext(db=mock_db)

    mock_ctx = MagicMock()
    mock_ctx.request_context.lifespan_context = app_context

    return mock_ctx


@pytest.mark.asyncio
async def test_find_all_users_empty(mock_context):
    """Test finding all users when database is empty."""
    result = await find_all_users(mock_context)
    assert result == []


@pytest.mark.asyncio
async def test_find_all_users_with_data(mock_context, async_db_session):
    """Test finding all users with existing data."""
    # Add test users
    user1 = User(first_name="John", last_name="Doe", email="john@test.com", age=30)
    user2 = User(first_name="Jane", last_name="Smith", email="jane@test.com", age=25)
    async_db_session.add_all([user1, user2])
    await async_db_session.commit()

    result = await find_all_users(mock_context)

    assert len(result) == 2
    assert all(isinstance(user, UserDto) for user in result)
    assert result[0].first_name == "John"
    assert result[1].first_name == "Jane"


@pytest.mark.asyncio
async def test_find_user_by_last_name_found(mock_context, async_db_session):
    """Test finding user by last name when user exists."""
    user = User(first_name="John", last_name="Doe", email="john@test.com", age=30)
    async_db_session.add(user)
    await async_db_session.commit()

    result = await find_user_by_last_name(mock_context, "Doe")

    assert result is not None
    assert isinstance(result, UserDto)
    assert result.first_name == "John"
    assert result.last_name == "Doe"


@pytest.mark.asyncio
async def test_find_user_by_last_name_not_found(mock_context):
    """Test finding user by last name when user doesn't exist."""
    result = await find_user_by_last_name(mock_context, "NonExistent")
    assert result is None


@pytest.mark.asyncio
async def test_add_user_success(mock_context, async_db_session):
    """Test adding a new user successfully."""
    await add_user(mock_context, "John", "Doe", "john@test.com", 30)

    # Verify user was added
    result = await async_db_session.execute(
        "SELECT * FROM users WHERE last_name = 'Doe'"
    )
    user = result.fetchone()
    assert user is not None


@pytest.mark.asyncio
async def test_delete_user_by_last_name_success(mock_context, async_db_session):
    """Test deleting existing user by last name."""
    user = User(first_name="John", last_name="Doe", email="john@test.com", age=30)
    async_db_session.add(user)
    await async_db_session.commit()

    result = await delete_user_by_last_name(mock_context, "Doe")

    assert result == "User 'Doe' deleted"


@pytest.mark.asyncio
async def test_delete_user_by_last_name_not_found(mock_context):
    """Test deleting non-existent user by last name."""
    result = await delete_user_by_last_name(mock_context, "NonExistent")
    assert result == "User 'NonExistent' not found"


@pytest.mark.asyncio
async def test_delete_all_users_with_data(mock_context, async_db_session):
    """Test deleting all users when users exist."""
    user1 = User(first_name="John", last_name="Doe", email="john@test.com", age=30)
    user2 = User(first_name="Jane", last_name="Smith", email="jane@test.com", age=25)
    async_db_session.add_all([user1, user2])
    await async_db_session.commit()

    result = await delete_all_users(mock_context)
    assert result == "2 users deleted"


@pytest.mark.asyncio
async def test_delete_all_users_empty_database(mock_context):
    """Test deleting all users when database is empty."""
    result = await delete_all_users(mock_context)
    assert result == "0 users deleted"


@pytest.mark.asyncio
async def test_get_database_stats_empty(mock_context):
    """Test getting database stats when empty."""
    result = await get_database_stats(mock_context)

    assert "Total users: 0" in result
    assert "Database: SQLite" in result
    assert "Status: Active" in result


@pytest.mark.asyncio
async def test_get_database_stats_with_data(mock_context, async_db_session):
    """Test getting database stats with existing users."""
    user1 = User(first_name="John", last_name="Doe", email="john@test.com", age=30)
    user2 = User(first_name="Jane", last_name="Smith", email="jane@test.com", age=25)
    async_db_session.add_all([user1, user2])
    await async_db_session.commit()

    result = await get_database_stats(mock_context)

    assert "Total users: 2" in result
    assert "Database: SQLite" in result
    assert "Status: Active" in result


@pytest.mark.asyncio
async def test_analyze_user_prompt():
    """Test analyze user prompt template."""
    result = await analyze_user_prompt("John Doe")

    assert "John Doe" in result
    assert "User behavior patterns" in result
    assert "Engagement metrics" in result
    assert "Recommendations" in result


@pytest.mark.asyncio
async def test_server_lifespan_context_creation():
    """Test that AppContext is properly created."""
    from database.connect import Database

    mock_db = MagicMock(spec=Database)
    app_context = AppContext(db=mock_db)

    assert app_context.db == mock_db
    assert isinstance(app_context, AppContext)


@pytest.mark.asyncio
async def test_user_dto_validation():
    """Test UserDto model validation with User data."""
    user = User(id=1, first_name="John", last_name="Doe", email="john@test.com", age=30)
    user_dto = UserDto.model_validate(user)

    assert user_dto.id == 1
    assert user_dto.first_name == "John"
    assert user_dto.last_name == "Doe"
    assert user_dto.email == "john@test.com"
    assert user_dto.age == 30
