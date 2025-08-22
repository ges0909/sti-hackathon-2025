from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from config import settings


class Database:
    """Database connection manager."""

    @classmethod
    async def connect(cls) -> "Database":
        """Connect to database."""
        print("🔌 Start SQLAlchemy Engine...")
        cls.engine = create_async_engine(settings.database_url, echo=True)
        cls.AsyncSessionLocal = async_sessionmaker(
            bind=cls.engine, expire_on_commit=False
        )
        return cls()

    async def disconnect(self) -> None:
        """Disconnect from database."""
        print("🧹 Close SQLAlchemy Engine...")
        if self.engine:
            await self.engine.dispose()

    def get_async_session(self) -> AsyncSession:
        """Get a database session."""
        return self.AsyncSessionLocal()
