import logging
from asyncio import CancelledError
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass

from database import user_repository
from database.connect import Database
from database.models.user import User
from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession
from schemas import UserDto

logger = logging.getLogger(__name__)


@dataclass
class AppContext:
    """Application context with typed dependencies."""

    db: Database


@asynccontextmanager
async def server_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """Manage application lifecycle with type-safe context."""

    db = await Database.connect()
    logger.info("🔗 Database connected")

    # Create tables
    logger.info("📋 Creating tables...")
    async with db.engine.begin() as conn:
        await conn.run_sync(User.metadata.create_all)
    logger.info("✅ Tables created")

    # Add initial data in separate transaction
    logger.info("👥 Adding initial users...")
    async with db.get_async_session() as session:
        user1 = User(name="gerrit", email="gerrit@mail.de", age=65)
        user2 = User(name="heike", email="heike@mail.de", age=60)
        session.add_all([user1, user2])
        await session.commit()
    logger.info("✅ Initial users added")

    try:
        yield AppContext(db=db)
    except CancelledError:
        logger.warning("⚠️ Server interrupted by user")
    finally:
        logger.info("🧹 Cleaning up database...")
        try:
            async with db.engine.begin() as conn:
                await conn.run_sync(User.metadata.drop_all)
            logger.info("✅ Database tables dropped")
        except (CancelledError, Exception):
            logger.warning("⚠️ Cleanup cancelled or failed")

        try:
            await db.disconnect()
            logger.info("✅ Database disconnected")
        except (CancelledError, Exception):
            logger.warning("⚠️ Disconnect cancelled or failed")


# Pass mcp-server to server
mcp = FastMCP("Lifespan Demo", lifespan=server_lifespan)


@mcp.tool(name="Find all users", description="Get all users from database.")
async def find_all_users(ctx: Context[ServerSession, AppContext]) -> list[UserDto]:
    """Get all users from database."""
    db = ctx.request_context.lifespan_context.db
    async with db.get_async_session() as session:
        users = await user_repository.get_all_users(session)
        return [UserDto.model_validate(user) for user in users]


@mcp.tool(name="Find user by name", description="Get an user by name.")
async def find_user_by_name(
    ctx: Context[ServerSession, AppContext], name: str
) -> UserDto | None:
    """Get user by name."""
    db = ctx.request_context.lifespan_context.db
    async with db.get_async_session() as session:
        user = await user_repository.get_user_by_name(session, name)
        if user:
            return UserDto.model_validate(user)
        return None


@mcp.tool(
    name="Add a user",
    description="Add a user with name, email and age to the database.",
)
async def add_user(
    ctx: Context[ServerSession, AppContext], name: str, email: str, age: int
) -> None:
    """Tool that uses initialized resources."""
    db = ctx.request_context.lifespan_context.db
    async with db.get_async_session() as session:
        await user_repository.add_user(session, name=name, email=email, age=age)
        logger.info(f"✅ User '{name}' added.")


@mcp.tool(
    name="Delete user by name", description="Delete a user by name from the database."
)
async def delete_user_by_name(
    ctx: Context[ServerSession, AppContext], name: str
) -> str:
    """Delete a user by name from the database."""
    db = ctx.request_context.lifespan_context.db
    async with db.get_async_session() as session:
        deleted = await user_repository.delete_user_by_name(session, name)
        if deleted:
            logger.info(f"✅ User '{name}' deleted.")
            return f"User '{name}' deleted"
        else:
            logger.info(f"⚠️ User '{name}' not found.")
            return f"User '{name}' not found"


@mcp.tool(name="Delete all users", description="Deletes all users from the database.")
async def delete_all_users(ctx: Context[ServerSession, AppContext]) -> str:
    """Deletes all users from the database."""
    db = ctx.request_context.lifespan_context.db
    async with db.get_async_session() as session:
        deleted_count = await user_repository.delete_all_users(session)
        logger.info(f"✅ {deleted_count} users have been deleted.")
        return f"{deleted_count} users deleted"


# Resources are static content. If you need dynamic data in resources, you have to define the URI with parameters.
@mcp.resource("user://database/stats")
async def user_stats() -> str:
    """Resource providing user database statistics."""
    return "Total users: Dynamic\nDatabase: SQLite\nStatus: Active"


# Prompts are templates with parameters.
@mcp.prompt("analyze-user")
async def analyze_user_prompt(name: str) -> str:
    """Prompt template for analyzing a specific user."""
    return f"Analyze this user profile for: {name}\n\nPlease provide insights on:\n- User behavior patterns\n- Engagement metrics\n- Recommendations"
