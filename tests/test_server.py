import pytest
import pytest_asyncio
from unittest.mock import MagicMock
from database.model.base_model import Base
from database.model.user_model import User, Gender
from database.model.address_model import Address
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.future import select
from server import (
    AppContext,
    find_all_users,
    find_user_by_last_name,
    add_user,
    update_user,
    delete_user_by_last_name,
    delete_all_users,
    find_all_addresses,
    find_address_by_id,
    add_address,
    update_address,
    delete_address_by_id,
    get_database_stats,
    analyze_user_prompt,
)
from schemas import UserDto, AddressDto

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


@pytest_asyncio.fixture
async def mock_context(async_db_session):
    mock_db = MagicMock()
    mock_db.get_async_session.return_value.__aenter__.return_value = async_db_session

    app_context = AppContext(db=mock_db)
    mock_ctx = MagicMock()
    mock_ctx.request_context.lifespan_context = app_context
    return mock_ctx


@pytest.mark.asyncio
async def test_find_all_users_empty(mock_context):
    result = await find_all_users(mock_context)
    assert result == []


@pytest.mark.asyncio
async def test_add_user_success(mock_context, async_db_session):
    result = await add_user(mock_context, "John", "Doe", "john@test.com", 30)
    assert "added" in result

    db_result = await async_db_session.execute(select(User).where(User.last_name == "Doe"))
    user = db_result.scalars().first()
    assert user is not None


@pytest.mark.asyncio
async def test_find_user_by_last_name_found(mock_context, async_db_session):
    user = User(first_name="John", last_name="Doe", email="john@test.com", age=30)
    async_db_session.add(user)
    await async_db_session.commit()

    result = await find_user_by_last_name(mock_context, "Doe")
    assert result is not None
    assert result.first_name == "John"


@pytest.mark.asyncio
async def test_update_user_success(mock_context, async_db_session):
    user = User(first_name="John", last_name="Doe", email="john@test.com", age=30, gender=Gender.MALE)
    async_db_session.add(user)
    await async_db_session.commit()

    result = await update_user(mock_context, "Doe", first_name="Johnny", age=31)
    assert "updated" in result


@pytest.mark.asyncio
async def test_delete_user_by_last_name_success(mock_context, async_db_session):
    user = User(first_name="John", last_name="Doe", email="john@test.com", age=30)
    async_db_session.add(user)
    await async_db_session.commit()

    result = await delete_user_by_last_name(mock_context, "Doe")
    assert "deleted" in result


@pytest.mark.asyncio
async def test_find_all_addresses_empty(mock_context):
    result = await find_all_addresses(mock_context)
    assert result == []


@pytest.mark.asyncio
async def test_add_address_success(mock_context, async_db_session):
    result = await add_address(mock_context, "123 Main St", "Test City", "12345", "Test Country", 1)
    assert "added" in result

    db_result = await async_db_session.execute(select(Address).where(Address.street == "123 Main St"))
    address = db_result.scalars().first()
    assert address is not None


@pytest.mark.asyncio
async def test_find_address_by_id_found(mock_context, async_db_session):
    address = Address(
        street="123 Main St",
        city="Test City", 
        postal_code="12345",
        country="Test Country",
        user_id=1
    )
    async_db_session.add(address)
    await async_db_session.commit()
    await async_db_session.refresh(address)

    result = await find_address_by_id(mock_context, address.id)
    assert result is not None
    assert result.street == "123 Main St"


@pytest.mark.asyncio
async def test_get_database_stats(mock_context, async_db_session):
    user = User(first_name="John", last_name="Doe", email="john@test.com", age=30)
    address = Address(street="123 Main St", city="Test City", postal_code="12345", country="Test Country", user_id=1)
    async_db_session.add_all([user, address])
    await async_db_session.commit()

    result = await get_database_stats(mock_context)
    assert "Total users: 1" in result
    assert "Total addresses: 1" in result


@pytest.mark.asyncio
async def test_analyze_user_prompt():
    result = await analyze_user_prompt("John Doe")
    assert "John Doe" in result
    assert "User behavior patterns" in result