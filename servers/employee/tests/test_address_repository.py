import pytest
import pytest_asyncio
from repositories.address_repository import address_repository
from models import Base
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
async def test_create_and_get_address(async_db_session):
    """Test creating an address and retrieving it by ID."""
    await address_repository.create(
        async_db_session,
        street="123 Main St",
        city="Test City",
        postal_code="12345",
        country="Test Country",
        user_id=1,
    )

    addresses = await address_repository.get_all(async_db_session)
    assert len(addresses) == 1

    address = addresses[0]
    assert address.street == "123 Main St"
    assert address.city == "Test City"
    assert address.postal_code == "12345"
    assert address.country == "Test Country"
    assert address.user_id == 1


@pytest.mark.asyncio
async def test_get_address_by_id(async_db_session):
    """Test getting address by ID."""
    await address_repository.create(
        async_db_session,
        street="456 Oak Ave",
        city="Another City",
        postal_code="67890",
        country="Another Country",
        user_id=2,
    )

    addresses = await address_repository.get_all(async_db_session)
    address_id = addresses[0].id

    address = await address_repository.get_by_id(async_db_session, address_id)
    assert address is not None
    assert address.street == "456 Oak Ave"


@pytest.mark.asyncio
async def test_update_address(async_db_session):
    """Test updating an address."""
    await address_repository.create(
        async_db_session,
        street="789 Pine St",
        city="Old City",
        postal_code="11111",
        country="Old Country",
        user_id=3,
    )

    addresses = await address_repository.get_all(async_db_session)
    address_id = addresses[0].id

    updated = await address_repository.update_by_id(
        async_db_session,
        address_id=address_id,
        city="New City",
        country="New Country",
    )
    assert updated is True

    address = await address_repository.get_by_id(async_db_session, address_id)
    assert address.street == "789 Pine St"  # unchanged
    assert address.city == "New City"  # updated
    assert address.country == "New Country"  # updated


@pytest.mark.asyncio
async def test_delete_address(async_db_session):
    """Test deleting an address."""
    await address_repository.create(
        async_db_session,
        street="Delete St",
        city="Delete City",
        postal_code="99999",
        country="Delete Country",
        user_id=4,
    )

    addresses = await address_repository.get_all(async_db_session)
    address_id = addresses[0].id

    deleted = await address_repository.delete_by_id(async_db_session, address_id)
    assert deleted is True

    address = await address_repository.get_by_id(async_db_session, address_id)
    assert address is None


@pytest.mark.asyncio
async def test_get_address_by_user_id(async_db_session):
    """Test getting address by user ID."""
    await address_repository.create(
        async_db_session,
        street="User St",
        city="User City",
        postal_code="55555",
        country="User Country",
        user_id=5,
    )

    address = await address_repository.get_by_user_id(async_db_session, 5)
    assert address is not None
    assert address.street == "User St"
    assert address.user_id == 5
