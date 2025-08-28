import pytest
import pytest_asyncio
from models import Base
from models import User
from models import Address
from services.user_service import user_service
from services.address_service import address_service
from services.stats_service import stats_service
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"


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
async def test_user_service_create_user(async_db_session):
    """Test creating user through service."""
    result = await user_service.create_user(
        async_db_session, "John", "Doe", "john@example.com", 30
    )
    assert result == "User 'John Doe' added"


@pytest.mark.asyncio
async def test_user_service_get_all_users(async_db_session):
    """Test getting all users through service."""
    user = User(first_name="John", last_name="Doe", email="john@example.com", age=30)
    async_db_session.add(user)
    await async_db_session.commit()

    result = await user_service.get_all_users(async_db_session)
    assert len(result) == 1
    assert result[0].first_name == "John"


@pytest.mark.asyncio
async def test_user_service_update_user(async_db_session):
    """Test updating user through service."""
    user = User(first_name="John", last_name="Doe", email="john@example.com", age=30)
    async_db_session.add(user)
    await async_db_session.commit()

    result = await user_service.update_user(
        async_db_session, "Doe", first_name="Johnny", age=31
    )
    assert result == "User 'Doe' updated"


@pytest.mark.asyncio
async def test_address_service_create_address(async_db_session):
    """Test creating address through service."""
    result = await address_service.create_address(
        async_db_session, "123 Main St", "New York", "10001", "USA", 1
    )
    assert result == "Address '123 Main St, New York' added"





@pytest.mark.asyncio
async def test_stats_service(async_db_session):
    """Test stats service."""
    user = User(first_name="John", last_name="Doe", email="john@example.com", age=30)
    address = Address(street="123 Main St", city="NYC", postal_code="10001", country="USA", user_id=1)
    async_db_session.add_all([user, address])
    await async_db_session.commit()

    result = await stats_service.get_database_stats(async_db_session)
    assert "Total users: 1" in result
    assert "Total addresses: 1" in result