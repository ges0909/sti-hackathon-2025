from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from database.models.user import User


async def get_all_users(session: AsyncSession) -> list[User]:
    """Get all users from the database."""
    result = await session.execute(select(User))
    return list(result.scalars().all())


async def get_user_by_name(session: AsyncSession, name: str) -> User | None:
    """Get user by name from the database."""
    result = await session.execute(select(User).where(User.name == name))
    return result.scalars().first()


async def add_user(session: AsyncSession, name: str, email: str, age: int) -> None:
    """Add a new user to the database."""
    try:
        user = User(name=name, email=email, age=age)
        session.add(user)
        await session.commit()
    except Exception:
        await session.rollback()
        raise
