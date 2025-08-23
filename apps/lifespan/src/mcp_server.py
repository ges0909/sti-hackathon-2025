"""Example showing lifespan support for startup/shutdown with strong typing."""

import os
from asyncio import CancelledError
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass

from config import settings
from database import user_repository
from database.connect import Database
from database.models.user import User
from logger import setup_logging
from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession
from mcp_tools.schemas import UserDto

# Setup logging
logger = setup_logging(settings.log_level)


@dataclass
class AppContext:
    """Application context with typed dependencies."""

    db: Database


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """Manage application lifecycle with type-safe context."""

    # Ensure data directory exists (important when using 'sqlite')
    os.makedirs("data", exist_ok=True)
    logger.info("📁 Data directory created")

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


# Pass lifespan to server
mcp = FastMCP("Lifespan Demo", lifespan=app_lifespan)


@mcp.tool()
async def get_all_users(ctx: Context[ServerSession, AppContext]) -> list[UserDto]:
    """Get all users from database."""
    db = ctx.request_context.lifespan_context.db
    async with db.get_async_session() as session:
        users = await user_repository.get_all_users(session)
        return [UserDto.model_validate(user) for user in users]


# Access type-safe lifespan context in mcp_tools
@mcp.tool()
async def get_user_by_name(
    ctx: Context[ServerSession, AppContext], name: str
) -> UserDto | None:
    """Get user by name."""
    db = ctx.request_context.lifespan_context.db
    async with db.get_async_session() as session:
        user = await user_repository.get_user_by_name(session, name)
        if user:
            return UserDto.model_validate(user)
        return None  #


@mcp.tool()
async def add_user(ctx: Context[ServerSession, AppContext], user: UserDto) -> None:
    """Tool that uses initialized resources."""
    db = ctx.request_context.lifespan_context.db
    async with db.get_async_session() as session:
        await user_repository.add_user(session, **user.model_dump())
