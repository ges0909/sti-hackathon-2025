import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from config import settings
from database.models.base import Base


class Database:
    """Database connection manager."""

    @classmethod
    async def connect(cls) -> "Database":
        """Connect to database."""

        cls.engine = create_async_engine(settings.database_url)
        await cls.engine.connect()
        cls.sessionLocal: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=cls.engine, class_=AsyncSession, expire_on_commit=False
        )
        async with cls.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        return cls()

    async def disconnect(self) -> None:
        """Disconnect from database."""
        if self.engine:
            await self.engine.dispose()

    def get_session(self) -> AsyncSession:
        """Get a database session."""
        return self.sessionLocal()
