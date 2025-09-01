import logging
from pathlib import Path
from urllib.parse import urlparse

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from config import settings

logger = logging.getLogger(__name__)


class Database:
    @classmethod
    async def connect(cls) -> "Database":
        logger.info("🔌 Start SQLAlchemy Engine...")
        _create_db_directory(settings.database_url)
        cls.engine = create_async_engine(
            settings.database_url,
            pool_size=20,
            max_overflow=30,
            pool_pre_ping=True,
            pool_recycle=3600,
            echo=settings.log_level == "DEBUG",
        )
        cls.async_session_local = async_sessionmaker(
            bind=cls.engine, expire_on_commit=False
        )
        return cls()

    async def disconnect(self) -> None:
        logger.info("🧹 Close SQLAlchemy Engine...")
        if self.engine:
            await self.engine.dispose()

    def get_async_session(self) -> AsyncSession:
        return self.async_session_local()


def _create_db_directory(db_url: str) -> None:
    file_path = urlparse(db_url).path.lstrip("/")
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    logger.info("📁 Data directory exists or created")
