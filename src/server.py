import logging
from asyncio import CancelledError
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass

from database import user_repository
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
    description="Add a user with name, email and age to the database.",
)
async def add_user(
    ctx: Context[ServerSession, AppContext],
    first_name: str,
    last_name: str,
    email: str,
    age: int,
) -> None:
    async with _get_db(ctx).get_async_session() as session:
        await user_repository.add_user(
            session, first_name=first_name, last_name=last_name, email=email, age=age
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
) -> str:
    async with _get_db(ctx).get_async_session() as session:
        updated = await user_repository.update_user(
            session, last_name=last_name, first_name=first_name, email=email, age=age
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


@mcp.tool(name="Get database stats", description="Get current database statistics.")
async def get_database_stats(ctx: Context[ServerSession, AppContext]) -> str:
    async with _get_db(ctx).get_async_session() as session:
        users = await user_repository.get_all_users(session)
        count = len(users)
    return f"Total users: {count}\nDatabase: SQLite\nStatus: Active"


@mcp.prompt("analyze-user")
async def analyze_user_prompt(name: str) -> str:
    return f"Analyze this user profile for: {name}\n\nPlease provide insights on:\n- User behavior patterns\n- Engagement metrics\n- Recommendations"
