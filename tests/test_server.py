import pytest
import pytest_asyncio
from unittest.mock import MagicMock
from database.model.base import Base
from database.model.user import User
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
from database.model.address import Address
from database.model.user import Gender

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
    result = await add_user(mock_context, "John", "Doe", "john@test.com", 30)
    assert "added" in result

    # Verify user was added
    db_result = await async_db_session.execute(select(User).where(User.last_name == "Doe"))
    user = db_result.scalars().first()
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
async def test_update_user_success(mock_context, async_db_session):
    """Test updating existing user successfully."""
    user = User(
        first_name="John",
        last_name="Doe",
        email="john@test.com",
        age=30,
        gender=Gender.MALE,
    )
    async_db_session.add(user)
    await async_db_session.commit()

    result = await update_user(mock_context, "Doe", first_name="Johnny", age=31)
    assert result == "User 'Doe' updated"


@pytest.mark.asyncio
async def test_update_user_not_found(mock_context):
    """Test updating non-existent user."""
    result = await update_user(mock_context, "NonExistent", first_name="New")
    assert result == "User 'NonExistent' not found"


@pytest.mark.asyncio
async def test_add_user_with_gender(mock_context, async_db_session):
    """Test adding user with gender field."""
    result = await add_user(mock_context, "Jane", "Smith", "jane@test.com", 25, Gender.FEMALE)
    assert "added" in result

    db_result = await async_db_session.execute(
        select(User).where(User.last_name == "Smith")
    )
    user = db_result.scalars().first()
    assert user is not None
    assert user.gender == Gender.FEMALE


@pytest.mark.asyncio
async def test_find_all_addresses_empty(mock_context):
    """Test finding all addresses when database is empty."""
    result = await find_all_addresses(mock_context)
    assert result == []


@pytest.mark.asyncio
async def test_find_all_addresses_with_data(mock_context, async_db_session):
    """Test finding all addresses with existing data."""
    address1 = Address(
        street="123 Main St",
        city="City1",
        postal_code="12345",
        country="Country1",
        user_id=1,
    )
    address2 = Address(
        street="456 Oak Ave",
        city="City2",
        postal_code="67890",
        country="Country2",
        user_id=2,
    )
    async_db_session.add_all([address1, address2])
    await async_db_session.commit()

    result = await find_all_addresses(mock_context)

    assert len(result) == 2
    assert all(isinstance(addr, AddressDto) for addr in result)
    assert result[0].street == "123 Main St"
    assert result[1].street == "456 Oak Ave"


@pytest.mark.asyncio
async def test_find_address_by_id_found(mock_context, async_db_session):
    """Test finding address by ID when address exists."""
    address = Address(
        street="123 Main St",
        city="Test City",
        postal_code="12345",
        country="Test Country",
        user_id=1,
    )
    async_db_session.add(address)
    await async_db_session.commit()
    await async_db_session.refresh(address)

    result = await find_address_by_id(mock_context, address.id)

    assert result is not None
    assert isinstance(result, AddressDto)
    assert result.street == "123 Main St"
    assert result.city == "Test City"


@pytest.mark.asyncio
async def test_find_address_by_id_not_found(mock_context):
    """Test finding address by ID when address doesn't exist."""
    result = await find_address_by_id(mock_context, 999)
    assert result is None


@pytest.mark.asyncio
async def test_add_address_success(mock_context, async_db_session):
    """Test adding a new address successfully."""
    result = await add_address(
        mock_context, "123 Main St", "Test City", "12345", "Test Country", 1
    )
    assert result == "Address '123 Main St, Test City' added"

    # Verify address was added
    from sqlalchemy import select

    result = await async_db_session.execute(
        select(Address).where(Address.street == "123 Main St")
    )
    address = result.scalars().first()
    assert address is not None


@pytest.mark.asyncio
async def test_update_address_success(mock_context, async_db_session):
    """Test updating existing address successfully."""
    address = Address(
        street="123 Main St",
        city="Old City",
        postal_code="12345",
        country="Old Country",
        user_id=1,
    )
    async_db_session.add(address)
    await async_db_session.commit()
    await async_db_session.refresh(address)

    result = await update_address(
        mock_context, address.id, city="New City", country="New Country"
    )
    assert result == f"Address ID {address.id} updated"


@pytest.mark.asyncio
async def test_update_address_not_found(mock_context):
    """Test updating non-existent address."""
    result = await update_address(mock_context, 999, city="New City")
    assert result == "Address ID 999 not found"


@pytest.mark.asyncio
async def test_delete_address_by_id_success(mock_context, async_db_session):
    """Test deleting existing address by ID."""
    address = Address(
        street="123 Main St",
        city="Test City",
        postal_code="12345",
        country="Test Country",
        user_id=1,
    )
    async_db_session.add(address)
    await async_db_session.commit()
    await async_db_session.refresh(address)

    result = await delete_address_by_id(mock_context, address.id)
    assert result == f"Address ID {address.id} deleted"


@pytest.mark.asyncio
async def test_delete_address_by_id_not_found(mock_context):
    """Test deleting non-existent address by ID."""
    result = await delete_address_by_id(mock_context, 999)
    assert result == "Address ID 999 not found"


@pytest.mark.asyncio
async def test_get_database_stats_with_addresses(mock_context, async_db_session):
    """Test getting database stats with users and addresses."""
    user = User(first_name="John", last_name="Doe", email="john@test.com", age=30)
    address = Address(
        street="123 Main St",
        city="Test City",
        postal_code="12345",
        country="Test Country",
        user_id=1,
    )
    async_db_session.add_all([user, address])
    await async_db_session.commit()

    result = await get_database_stats(mock_context)

    assert "Total users: 1" in result
    assert "Total addresses: 1" in result
    assert "Database: SQLite" in result
    assert "Status: Active" in result


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


@pytest.mark.asyncio
async def test_address_dto_validation():
    """Test AddressDto model validation with Address data."""
    address = Address(
        id=1,
        street="123 Main St",
        city="Test City",
        postal_code="12345",
        country="Test Country",
        user_id=1,
    )
    address_dto = AddressDto.model_validate(address)

    assert address_dto.id == 1
    assert address_dto.street == "123 Main St"
    assert address_dto.city == "Test City"
    assert address_dto.postal_code == "12345"
    assert address_dto.country == "Test Country"
    assert address_dto.user_id == 1
