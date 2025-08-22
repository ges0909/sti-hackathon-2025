"""Example showing lifespan support for startup/shutdown with strong typing."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass

from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession

from database import repository
from database.connect import Database
from database.models.user import User

import os


@dataclass
class AppContext:
    """Application context with typed dependencies."""

    db: Database


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """Manage application lifecycle with type-safe context."""

    # Ensure data directory exists (important when using 'sqlite')
    os.makedirs("data", exist_ok=True)
    print("📁 Data directory created")

    db = await Database.connect()
    print("🔗 Database connected")

    # Create tables
    print("📋 Creating tables...")
    async with db.engine.begin() as conn:
        await conn.run_sync(User.metadata.create_all)
    print("✅ Tables created")

    # Add initial data in separate transaction
    print("👥 Adding initial users...")
    async with db.get_async_session() as session:
        user1 = User(name="gerrit", email="gerrit@mail.de", age=65)
        user2 = User(name="heike", email="heike@mail.de", age=60)
        session.add_all([user1, user2])
        await session.commit()
    print("✅ Initial users added")

    try:
        yield AppContext(db=db)
    finally:
        print("🧹 Cleaning up database...")
        async with db.engine.begin() as conn:
            await conn.run_sync(User.metadata.drop_all)
        print("✅ Database cleaned up")
        await db.disconnect()


# Pass lifespan to server
mcp = FastMCP("Lifespan Demo", lifespan=app_lifespan)


# Access type-safe lifespan context in tools
@mcp.tool()
async def query_db(ctx: Context[ServerSession, AppContext]):
    """Tool that uses initialized resources."""
    db = ctx.request_context.lifespan_context.db
    async with db.get_async_session() as session:
        user = await repository.get_user(session)
        if user:
            return user
        return None


@mcp.tool()
async def add_user(ctx: Context[ServerSession, AppContext], user) -> None:
    """Tool that uses initialized resources."""
    db = ctx.request_context.lifespan_context.db
    async with db.get_async_session() as session:
        await repository.add_user(session, **user.model_dump())
