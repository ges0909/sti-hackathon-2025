from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from db.models.user import User


async def add_user(session: AsyncSession, name: str, email: str, age: int) -> None:
    """Add a new user to the db."""
    try:
        user = User(name=name, email=email, age=age)
        session.add(user)
        await session.commit()
    except Exception:
        await session.rollback()
        raise


async def get_user(session: AsyncSession) -> User | None:
    """Get the first user from the db."""
    result = await session.execute(select(User))
    return result.scalars().first()
