import logging
from asyncio import CancelledError
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass

from connect import Database
from models import User, Address, Base
from models import Gender
from config import settings
from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession
from schemas import UserDto, AddressDto
from services.user_service import user_service
from services.address_service import address_service
from services.stats_service import stats_service
from faker import Faker

logger = logging.getLogger(__name__)


@dataclass
class AppContext:
    db: Database


@asynccontextmanager
async def server_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    db = await Database.connect()
    logger.info("✅ Database connected")

    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("✅ Tables created")

    async with db.get_async_session() as session:
        fake = Faker()
        users = [
            User(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                age=fake.random_int(18, 80),
                gender=fake.random_element([Gender.MALE, Gender.FEMALE, Gender.OTHER]),
                address=Address(
                    street=fake.street_address(),
                    city=fake.city(),
                    postal_code=fake.postcode(),
                    country=fake.country(),
                ),
            )
            for _ in range(settings.initial_users_count)
        ]
        session.add_all(users)
        await session.commit()
    logger.info(f"✅ {len(users)} users added")

    try:
        yield AppContext(db=db)
    except (CancelledError, Exception):
        logger.warning("⚠️ Server interrupted")
        try:
            async with db.engine.begin() as conn:
                await conn.run_sync(User.metadata.drop_all)
                logger.info("✅ Tables dropped")
        except (CancelledError, Exception):
            pass
        await db.disconnect()
        logger.info("✅ Database disconnected")


mcp = FastMCP("Lifespan Demo", lifespan=server_lifespan)


def _get_db(ctx: Context[ServerSession, AppContext]) -> Database:
    return ctx.request_context.lifespan_context.db


@mcp.tool(name="Find all users", description="Get all users from database.")
async def find_all_users(ctx: Context[ServerSession, AppContext]) -> list[UserDto]:
    async with _get_db(ctx).get_async_session() as session:
        return await user_service.get_all_users(session)


@mcp.tool(name="Find user by last name", description="Get an user by name.")
async def find_user_by_last_name(
    ctx: Context[ServerSession, AppContext], name: str
) -> UserDto | None:
    async with _get_db(ctx).get_async_session() as session:
        return await user_service.get_user_by_last_name(session, name)


@mcp.tool(
    name="Add a user",
    description="Add a user with name, email, age and gender to the database.",
)
async def add_user(
    ctx: Context[ServerSession, AppContext],
    first_name: str,
    last_name: str,
    email: str,
    age: int,
    gender: str = None,
) -> str:
    try:
        async with _get_db(ctx).get_async_session() as session:
            result = await user_service.create_user(
                session, first_name, last_name, email, age, gender
            )
            logger.info(f"✅ {result}")
            return result
    except ValueError as e:
        logger.error(str(e))
        return str(e)


@mcp.tool(
    name="Update user",
    description="Update a user by last name with optional new values.",
)
async def update_user(
    ctx: Context[ServerSession, AppContext],
    last_name: str,
    first_name: str = None,
    email: str = None,
    age: int = None,
    gender: str = None,
) -> str:
    try:
        async with _get_db(ctx).get_async_session() as session:
            result = await user_service.update_user(
                session, last_name, first_name, email, age, gender
            )
            if "updated" in result:
                logger.info(f"✅ {result}")
            else:
                logger.warning(f"⚠️ {result}")
            return result
    except ValueError as e:
        logger.error(str(e))
        return str(e)


@mcp.tool(
    name="Delete user by last name",
    description="Delete a user by last name from the database.",
)
async def delete_user_by_last_name(
    ctx: Context[ServerSession, AppContext], last_name: str
) -> str:
    async with _get_db(ctx).get_async_session() as session:
        result = await user_service.delete_user_by_last_name(session, last_name)
        if "deleted" in result:
            logger.info(f"✅ {result}")
        else:
            logger.warning(f"⚠️ {result}")
        return result


@mcp.tool(name="Delete all users", description="Deletes all users from the database.")
async def delete_all_users(ctx: Context[ServerSession, AppContext]) -> str:
    async with _get_db(ctx).get_async_session() as session:
        result = await user_service.delete_all_users(session)
        logger.info(f"✅ {result}")
        return result


@mcp.tool(name="Find all addresses", description="Get all addresses from database.")
async def find_all_addresses(
    ctx: Context[ServerSession, AppContext],
) -> list[AddressDto]:
    async with _get_db(ctx).get_async_session() as session:
        return await address_service.get_all_addresses(session)


@mcp.tool(name="Find address by ID", description="Get address by ID.")
async def find_address_by_id(
    ctx: Context[ServerSession, AppContext], address_id: int
) -> AddressDto | None:
    async with _get_db(ctx).get_async_session() as session:
        return await address_service.get_address_by_id(session, address_id)


@mcp.tool(name="Add address", description="Add a new address to the database.")
async def add_address(
    ctx: Context[ServerSession, AppContext],
    street: str,
    city: str,
    postal_code: str,
    country: str,
    user_id: int,
) -> str:
    try:
        async with _get_db(ctx).get_async_session() as session:
            result = await address_service.create_address(
                session, street, city, postal_code, country, user_id
            )
            logger.info(f"✅ {result}")
            return result
    except ValueError as e:
        logger.error(str(e))
        return str(e)


@mcp.tool(name="Update address", description="Update an address by ID.")
async def update_address(
    ctx: Context[ServerSession, AppContext],
    address_id: int,
    street: str = None,
    city: str = None,
    postal_code: str = None,
    country: str = None,
) -> str:
    try:
        async with _get_db(ctx).get_async_session() as session:
            result = await address_service.update_address(
                session, address_id, street, city, postal_code, country
            )
            if "updated" in result:
                logger.info(f"✅ {result}")
            else:
                logger.warning(f"⚠️ {result}")
            return result
    except ValueError as e:
        logger.error(str(e))
        return str(e)


@mcp.tool(name="Delete address by ID", description="Delete an address by ID.")
async def delete_address_by_id(
    ctx: Context[ServerSession, AppContext], address_id: int
) -> str:
    async with _get_db(ctx).get_async_session() as session:
        result = await address_service.delete_address_by_id(session, address_id)
        if "deleted" in result:
            logger.info(f"✅ {result}")
        else:
            logger.warning(f"⚠️ {result}")
        return result


@mcp.tool(name="Get database stats", description="Get current database statistics.")
async def get_database_stats(ctx: Context[ServerSession, AppContext]) -> str:
    async with _get_db(ctx).get_async_session() as session:
        return await stats_service.get_database_stats(session)


@mcp.prompt("analyze-user")
async def analyze_user_prompt(name: str) -> str:
    return f"Analyze this user profile for: {name}\n\nPlease provide insights on:\n- User behavior patterns\n- Engagement metrics\n- Recommendations"
