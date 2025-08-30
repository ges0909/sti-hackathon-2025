import pytest
import pytest_asyncio
from models import Base, User, WorkStatus
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.future import select

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
async def test_create_work_status(async_db_session):
    """Test creating a work status."""
    work_status = WorkStatus(is_home_office=True, user_id=1)
    async_db_session.add(work_status)
    await async_db_session.commit()

    result = await async_db_session.execute(
        select(WorkStatus).where(WorkStatus.user_id == 1)
    )
    saved_status = result.scalars().first()
    assert saved_status is not None
    assert saved_status.is_home_office is True


@pytest.mark.asyncio
async def test_user_with_work_status(async_db_session):
    """Test user with work status relationship."""
    user = User(
        first_name="John",
        last_name="Doe", 
        email="john@test.com",
        age=30,
        work_status=WorkStatus(is_home_office=False)
    )
    async_db_session.add(user)
    await async_db_session.commit()
    
    # Query work status directly
    result = await async_db_session.execute(
        select(WorkStatus).where(WorkStatus.user_id == user.id)
    )
    work_status = result.scalars().first()
    
    assert work_status is not None
    assert work_status.is_home_office is False
    assert work_status.user_id == user.id


@pytest.mark.asyncio
async def test_update_work_status(async_db_session):
    """Test updating work status."""
    user = User(
        first_name="Jane",
        last_name="Smith",
        email="jane@test.com",
        work_status=WorkStatus(is_home_office=False)
    )
    async_db_session.add(user)
    await async_db_session.commit()

    # Get work status and update
    result = await async_db_session.execute(
        select(WorkStatus).where(WorkStatus.user_id == user.id)
    )
    work_status = result.scalars().first()
    work_status.is_home_office = True
    await async_db_session.commit()

    # Verify update
    result = await async_db_session.execute(
        select(WorkStatus).where(WorkStatus.user_id == user.id)
    )
    updated_status = result.scalars().first()
    assert updated_status.is_home_office is True


@pytest.mark.asyncio
async def test_user_without_work_status(async_db_session):
    """Test user without work status (optional relationship)."""
    user = User(
        first_name="Bob",
        last_name="Wilson",
        email="bob@test.com",
        age=25
    )
    async_db_session.add(user)
    await async_db_session.commit()

    # Query work status directly
    result = await async_db_session.execute(
        select(WorkStatus).where(WorkStatus.user_id == user.id)
    )
    work_status = result.scalars().first()
    
    assert work_status is None


@pytest.mark.asyncio
async def test_work_status_unique_constraint(async_db_session):
    """Test that user_id is unique in work_status table."""
    work_status1 = WorkStatus(is_home_office=True, user_id=1)
    work_status2 = WorkStatus(is_home_office=False, user_id=1)
    
    async_db_session.add(work_status1)
    await async_db_session.commit()
    
    async_db_session.add(work_status2)
    
    with pytest.raises(Exception):  # Should raise integrity error
        await async_db_session.commit()


@pytest.mark.asyncio
async def test_work_status_default_value(async_db_session):
    """Test work status default value."""
    work_status = WorkStatus(user_id=1)
    async_db_session.add(work_status)
    await async_db_session.commit()

    result = await async_db_session.execute(
        select(WorkStatus).where(WorkStatus.user_id == 1)
    )
    saved_status = result.scalars().first()
    assert saved_status.is_home_office is False  # Default value