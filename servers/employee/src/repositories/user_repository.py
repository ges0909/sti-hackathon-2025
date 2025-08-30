from models.user import User
from repositories.base_repository import BaseRepository
from sqlalchemy import delete, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession


class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(User)

    async def get_by_last_name(
        self, session: AsyncSession, last_name: str
    ) -> User | None:
        result = await session.execute(select(User).where(User.last_name == last_name))
        return result.scalars().first()

    async def create(
        self,
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
            await self.add(session, user)
        except IntegrityError as err:
            await session.rollback()
            raise ValueError("Email already exists") from err

    async def update_by_last_name(
        self,
        session: AsyncSession,
        last_name: str,
        first_name: str = None,
        email: str = None,
        age: int = None,
        gender: str = None,
    ) -> bool:
        user = await self.get_by_last_name(session, last_name)
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
        except IntegrityError as err:
            await session.rollback()
            raise ValueError("Email already exists") from err

    async def delete_by_last_name(self, session: AsyncSession, last_name: str) -> bool:
        result = await session.execute(delete(User).where(User.last_name == last_name))
        await session.commit()
        return result.rowcount > 0


user_repository = UserRepository()
