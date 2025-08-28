import logging
from asyncio import CancelledError
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass

from database import user_repository, address_repository
from database.connect import Database
from database.models.user import User
from database.models.address import Address
from database.models.base import Base
from config import settings
from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession
from schemas import UserDto
from faker import Faker

logger = logging.getLogger(__name__)


@dataclass
class AppContext:
    db: Database


@asynccontextmanager
async def server_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    db = await Database.connect()
    logger.info("🔗 Database connected")

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
                gender=fake.random_element(["male", "female", "other"]),
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
        users = await user_repository.get_all_users(session)
        return [UserDto.model_validate(user) for user in users]


@mcp.tool(name="Find user by last name", description="Get an user by name.")
async def find_user_by_last_name(
    ctx: Context[ServerSession, AppContext], name: str
) -> UserDto | None:
    async with _get_db(ctx).get_async_session() as session:
        user = await user_repository.get_user_by_last_name(session, name)
        return UserDto.model_validate(user) if user else None


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
) -> None:
    async with _get_db(ctx).get_async_session() as session:
        await user_repository.add_user(
            session,
            first_name=first_name,
            last_name=last_name,
            email=email,
            age=age,
            gender=gender,
        )
        logger.info(f"✅ User '{first_name} {last_name}' added.")


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
    async with _get_db(ctx).get_async_session() as session:
        updated = await user_repository.update_user(
            session,
            last_name=last_name,
            first_name=first_name,
            email=email,
            age=age,
            gender=gender,
        )
        if updated:
            logger.info(f"✅ User '{last_name}' updated.")
            return f"User '{last_name}' updated"
        logger.warning(f"⚠️ User '{last_name}' not found.")
        return f"User '{last_name}' not found"


@mcp.tool(
    name="Delete user by last name",
    description="Delete a user by last name from the database.",
)
async def delete_user_by_last_name(
    ctx: Context[ServerSession, AppContext], last_name: str
) -> str:
    async with _get_db(ctx).get_async_session() as session:
        deleted = await user_repository.delete_user_by_last_name(session, last_name)
        if deleted:
            logger.info(f"✅ User '{last_name}' deleted.")
            return f"User '{last_name}' deleted"
        logger.info(f"⚠️ User '{last_name}' not found.")
        return f"User '{last_name}' not found"


@mcp.tool(name="Delete all users", description="Deletes all users from the database.")
async def delete_all_users(ctx: Context[ServerSession, AppContext]) -> str:
    async with _get_db(ctx).get_async_session() as session:
        deleted_count = await user_repository.delete_all_users(session)
        logger.info(f"✅ {deleted_count} users have been deleted.")
        return f"{deleted_count} users deleted"


@mcp.tool(name="Find all addresses", description="Get all addresses from database.")
async def find_all_addresses(ctx: Context[ServerSession, AppContext]) -> list[dict]:
    async with _get_db(ctx).get_async_session() as session:
        addresses = await address_repository.get_all_addresses(session)
        return [
            {
                "id": addr.id,
                "street": addr.street,
                "city": addr.city,
                "postal_code": addr.postal_code,
                "country": addr.country,
                "user_id": addr.user_id,
            }
            for addr in addresses
        ]


@mcp.tool(name="Find address by ID", description="Get address by ID.")
async def find_address_by_id(
    ctx: Context[ServerSession, AppContext], address_id: int
) -> dict | None:
    async with _get_db(ctx).get_async_session() as session:
        address = await address_repository.get_address_by_id(session, address_id)
        if address:
            return {
                "id": address.id,
                "street": address.street,
                "city": address.city,
                "postal_code": address.postal_code,
                "country": address.country,
                "user_id": address.user_id,
            }
        return None


@mcp.tool(name="Add address", description="Add a new address to the database.")
async def add_address(
    ctx: Context[ServerSession, AppContext],
    street: str,
    city: str,
    postal_code: str,
    country: str,
    user_id: int,
) -> str:
    async with _get_db(ctx).get_async_session() as session:
        await address_repository.add_address(
            session,
            street=street,
            city=city,
            postal_code=postal_code,
            country=country,
            user_id=user_id,
        )
        logger.info(f"✅ Address '{street}, {city}' added.")
        return f"Address '{street}, {city}' added"


@mcp.tool(name="Update address", description="Update an address by ID.")
async def update_address(
    ctx: Context[ServerSession, AppContext],
    address_id: int,
    street: str = None,
    city: str = None,
    postal_code: str = None,
    country: str = None,
) -> str:
    async with _get_db(ctx).get_async_session() as session:
        updated = await address_repository.update_address(
            session,
            address_id=address_id,
            street=street,
            city=city,
            postal_code=postal_code,
            country=country,
        )
        if updated:
            logger.info(f"✅ Address ID {address_id} updated.")
            return f"Address ID {address_id} updated"
        logger.warning(f"⚠️ Address ID {address_id} not found.")
        return f"Address ID {address_id} not found"


@mcp.tool(name="Delete address by ID", description="Delete an address by ID.")
async def delete_address_by_id(
    ctx: Context[ServerSession, AppContext], address_id: int
) -> str:
    async with _get_db(ctx).get_async_session() as session:
        deleted = await address_repository.delete_address_by_id(session, address_id)
        if deleted:
            logger.info(f"✅ Address ID {address_id} deleted.")
            return f"Address ID {address_id} deleted"
        logger.warning(f"⚠️ Address ID {address_id} not found.")
        return f"Address ID {address_id} not found"


@mcp.tool(name="Get database stats", description="Get current database statistics.")
async def get_database_stats(ctx: Context[ServerSession, AppContext]) -> str:
    async with _get_db(ctx).get_async_session() as session:
        users = await user_repository.get_all_users(session)
        addresses = await address_repository.get_all_addresses(session)
        user_count = len(users)
        address_count = len(addresses)
    return f"Total users: {user_count}\nTotal addresses: {address_count}\nDatabase: SQLite\nStatus: Active"


@mcp.prompt("analyze-user")
async def analyze_user_prompt(name: str) -> str:
    return f"Analyze this user profile for: {name}\n\nPlease provide insights on:\n- User behavior patterns\n- Engagement metrics\n- Recommendations"
