import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from database.repository import get_all_users, add_user
from database.models.user import User


@pytest_asyncio.fixture
async def db_session():
    """Create test database session."""
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    
    # Create tables
    async with engine.begin() as conn:
        await conn.run_sync(User.metadata.create_all)
    
    async_session_local = async_sessionmaker(bind=engine, expire_on_commit=False)
    session = async_session_local()
    
    try:
        yield session
    finally:
        await session.close()
        await engine.dispose()


@pytest.mark.asyncio
async def test_get_all_users_empty(db_session: AsyncSession):
    """Test get_all_users with empty database."""
    users = await get_all_users(db_session)
    assert users == []


@pytest.mark.asyncio
async def test_get_all_users(db_session: AsyncSession):
    """Test get_all_users with existing users."""
    # Add test users
    await add_user(db_session, "alice", "alice@test.com", 25)
    await add_user(db_session, "bob", "bob@test.com", 30)
    
    users = await get_all_users(db_session)
    
    assert len(users) == 2
    assert users[0].name == "alice"
    assert users[1].name == "bob"