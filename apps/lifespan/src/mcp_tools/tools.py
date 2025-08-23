# Access type-safe lifespan context in mcp_tools
from dataclasses import dataclass

from database import user_repository
from database.connect import Database
from mcp.server.fastmcp import Context
from mcp.server.session import ServerSession
from schemas import UserDto


@dataclass
class AppContext:
    """Application context with typed dependencies."""

    db: Database


async def get_all_users(ctx: Context[ServerSession, AppContext]) -> list[UserDto]:
    """Get all users from database."""
    db = ctx.request_context.lifespan_context.db
    async with db.get_async_session() as session:
        users = await user_repository.get_all_users(session)
        return [UserDto.model_validate(user) for user in users]


async def get_user_by_name(
    ctx: Context[ServerSession, AppContext], name: str
) -> UserDto | None:
    """Get user by name."""
    db = ctx.request_context.lifespan_context.db
    async with db.get_async_session() as session:
        user = await user_repository.get_user_by_name(session, name)
        if user:
            return UserDto.model_validate(user)
        return None


async def add_user(ctx: Context[ServerSession, AppContext], user: UserDto) -> None:
    """Tool that uses initialized resources."""
    db = ctx.request_context.lifespan_context.db
    async with db.get_async_session() as session:
        await user_repository.add_user(session, **user.model_dump())
