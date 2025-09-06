from sqlalchemy.ext.asyncio import AsyncSession
from employee.repositories.user_repository import user_repository
from employee.repositories.address_repository import address_repository


class StatsService:
    @staticmethod
    async def get_database_stats(session: AsyncSession) -> str:
        users = await user_repository.get_all(session)
        addresses = await address_repository.get_all(session)
        user_count = len(users)
        address_count = len(addresses)
        return f"""Total users: {user_count}
        Total addresses: {address_count}
        Database: SQLite
        Status: Active"""


stats_service = StatsService()
