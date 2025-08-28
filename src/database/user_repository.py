from database.models.user import User
from sqlalchemy import delete, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession


async def get_all_users(session: AsyncSession) -> list[User]:
    result = await session.execute(select(User))
    return list(result.scalars().all())


async def get_user_by_last_name(session: AsyncSession, last_name: str) -> User | None:
    result = await session.execute(select(User).where(User.last_name == last_name))
    return result.scalars().first()


async def add_user(
    session: AsyncSession,
    first_name: str,
    last_name: str,
    email: str,
    age: int,
    gender: str = None,
) -> None:
    try:
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            age=age,
            gender=gender,
        )
        session.add(user)
        await session.commit()
    except IntegrityError:
        await session.rollback()
        raise ValueError("Email already exists")


async def update_user(
    session: AsyncSession,
    last_name: str,
    first_name: str = None,
    email: str = None,
    age: int = None,
    gender: str = None,
) -> bool:
    user = await get_user_by_last_name(session, last_name)
    if not user:
        return False

    if first_name is not None:
        user.first_name = first_name
    if email is not None:
        user.email = email
    if age is not None:
        user.age = age
    if gender is not None:
        user.gender = gender

    try:
        await session.commit()
        return True
    except IntegrityError:
        await session.rollback()
        raise ValueError("Email already exists")


async def delete_user_by_last_name(session: AsyncSession, last_name: str) -> bool:
    result = await session.execute(delete(User).where(User.last_name == last_name))
    await session.commit()
    return result.rowcount > 0


async def delete_all_users(session: AsyncSession) -> int:
    result = await session.execute(delete(User))
    await session.commit()
    return result.rowcount
