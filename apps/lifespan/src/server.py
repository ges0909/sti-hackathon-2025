"""Example showing lifespan support for startup/shutdown with strong typing."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass

from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession

from database import repository, schemas
from database.connection import Database
from database.models.user import User


@dataclass
class AppContext:
    """Application context with typed dependencies."""

    db: Database


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """Manage application lifecycle with type-safe context."""
    db = await Database.connect()
    # Initialize on startup
    async with db.get_session() as session:
        await repository.add_user(session, name="gerrit", email="gerrit@mail.de", age=65)
        await repository.add_user(session, name="heike", email="heike@mail.de", age=60)
    try:
        yield AppContext(db=db)
    finally:
        # Cleanup on shutdown
        async with db.engine.begin() as conn:
            await conn.run_sync(User.metadata.drop_all)
        await db.disconnect()


# Pass lifespan to server
mcp = FastMCP("lifespan_demo", lifespan=app_lifespan)


# Access type-safe lifespan context in tools
@mcp.tool()
async def query_db(ctx: Context[ServerSession, AppContext]) -> schemas.User | None:
    """Tool that uses initialized resources."""
    db = ctx.request_context.lifespan_context.db
    async with db.get_session() as session:
        user = await repository.get_user(session)
        if user:
            return schemas.User.model_validate(user)
        return None


@mcp.tool()
async def add_user(
    ctx: Context[ServerSession, AppContext], user: schemas.UserBase
) -> None:
    """Tool that uses initialized resources."""
    db = ctx.request_context.lifespan_context.db
    async with db.get_session() as session:
        await repository.add_user(session, **user.model_dump())
