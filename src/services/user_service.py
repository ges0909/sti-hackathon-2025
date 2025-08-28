from sqlalchemy.ext.asyncio import AsyncSession
from database.repository.user_repository import user_repository
from schemas import UserDto


class UserService:
    async def get_all_users(self, session: AsyncSession) -> list[UserDto]:
        users = await user_repository.get_all(session)
        return [UserDto.model_validate(user) for user in users]

    async def get_user_by_last_name(self, session: AsyncSession, last_name: str) -> UserDto | None:
        user = await user_repository.get_by_last_name(session, last_name)
        return UserDto.model_validate(user) if user else None

    async def create_user(
        self,
        session: AsyncSession,
        first_name: str,
        last_name: str,
        email: str,
        age: int,
        gender: str = None,
    ) -> str:
        await user_repository.create(
            session,
            first_name=first_name,
            last_name=last_name,
            email=email,
            age=age,
            gender=gender,
        )
        return f"User '{first_name} {last_name}' added"

    async def update_user(
        self,
        session: AsyncSession,
        last_name: str,
        first_name: str = None,
        email: str = None,
        age: int = None,
        gender: str = None,
    ) -> str:
        updated = await user_repository.update_by_last_name(
            session,
            last_name=last_name,
            first_name=first_name,
            email=email,
            age=age,
            gender=gender,
        )
        if updated:
            return f"User '{last_name}' updated"
        return f"User '{last_name}' not found"

    async def delete_user_by_last_name(self, session: AsyncSession, last_name: str) -> str:
        deleted = await user_repository.delete_by_last_name(session, last_name)
        if deleted:
            return f"User '{last_name}' deleted"
        return f"User '{last_name}' not found"

    async def delete_all_users(self, session: AsyncSession) -> str:
        deleted_count = await user_repository.delete_all(session)
        return f"{deleted_count} users deleted"


user_service = UserService()
