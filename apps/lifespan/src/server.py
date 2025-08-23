"""Example showing lifespan support for startup/shutdown with strong typing."""

from asyncio import CancelledError
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass

from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession

from database import repository
from mcp_tools.schemas import UserDto
from database.connect import Database
from database.models.user import User

import os
import sys


@dataclass
class AppContext:
    """Application context with typed dependencies."""

    db: Database


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """Manage application lifecycle with type-safe context."""

    # Ensure data directory exists (important when using 'sqlite')
    os.makedirs("data", exist_ok=True)
    print("📁 Data directory created", file=sys.stderr)

    db = await Database.connect()
    print("🔗 Database connected", file=sys.stderr)

    # Create tables
    print("📋 Creating tables...", file=sys.stderr)
    async with db.engine.begin() as conn:
        await conn.run_sync(User.metadata.create_all)
    print("✅ Tables created", file=sys.stderr)

    # Add initial data in separate transaction
    print("👥 Adding initial users...", file=sys.stderr)
    async with db.get_async_session() as session:
        user1 = User(name="gerrit", email="gerrit@mail.de", age=65)
        user2 = User(name="heike", email="heike@mail.de", age=60)
        session.add_all([user1, user2])
        await session.commit()
    print("✅ Initial users added", file=sys.stderr)

    try:
        yield AppContext(db=db)
    except CancelledError:
        print("⚠️ Server interrupted by user", file=sys.stderr)
    finally:
        print("🧹 Cleaning up database...", file=sys.stderr)
        try:
            async with db.engine.begin() as conn:
                await conn.run_sync(User.metadata.drop_all)
            print("✅ Database tables dropped", file=sys.stderr)
        except (CancelledError, Exception):
            print("⚠️ Cleanup cancelled or failed", file=sys.stderr)

        try:
            await db.disconnect()
            print("✅ Database disconnected", file=sys.stderr)
        except (CancelledError, Exception):
            print("⚠️ Disconnect cancelled or failed", file=sys.stderr)


# Pass lifespan to server
mcp = FastMCP("Lifespan Demo", lifespan=app_lifespan)


@mcp.tool()
async def get_all_users(ctx: Context[ServerSession, AppContext]) -> list[UserDto]:
    """Get all users from database."""
    db = ctx.request_context.lifespan_context.db
    async with db.get_async_session() as session:
        users = await repository.get_all_users(session)
        return [UserDto.model_validate(user) for user in users]


# Access type-safe lifespan context in mcp_tools
@mcp.tool()
async def get_user_by_name(
    ctx: Context[ServerSession, AppContext], name: str
) -> UserDto | None:
    """Get user by name."""
    db = ctx.request_context.lifespan_context.db
    async with db.get_async_session() as session:
        user = await repository.get_user_by_name(session, name)
        if user:
            return UserDto.model_validate(user)
        return None  #


@mcp.tool()
async def add_user(ctx: Context[ServerSession, AppContext], user: UserDto) -> None:
    """Tool that uses initialized resources."""
    db = ctx.request_context.lifespan_context.db
    async with db.get_async_session() as session:
        await repository.add_user(session, **user.model_dump())
