from sqlalchemy.ext.asyncio import AsyncSession
from repositories.user_repository import user_repository
from repositories.address_repository import address_repository


class StatsService:
    async def get_database_stats(self, session: AsyncSession) -> str:
        users = await user_repository.get_all(session)
        addresses = await address_repository.get_all(session)
        user_count = len(users)
        address_count = len(addresses)
        return f"Total users: {user_count}\nTotal addresses: {address_count}\nDatabase: SQLite\nStatus: Active"


stats_service = StatsService()
