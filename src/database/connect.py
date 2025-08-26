from pathlib import Path
from urllib.parse import urlparse

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from config import settings
from logger import setup_logging

# Setup logging
logger = setup_logging(settings.log_level)


class Database:
    """Database connection manager."""

    @classmethod
    async def connect(cls) -> "Database":
        """Connect to database."""
        logger.info("🔌 Start SQLAlchemy Engine...")
        # Ensure data directory exists, which is important when using 'sqlite'
        extract_and_create_path_from_url(settings.database_url)
        cls.engine = create_async_engine(settings.database_url, echo=False)
        cls.AsyncSessionLocal = async_sessionmaker(
            bind=cls.engine, expire_on_commit=False
        )
        return cls()

    async def disconnect(self) -> None:
        """Disconnect from database."""
        logger.info("🧹 Close SQLAlchemy Engine...")
        if self.engine:
            await self.engine.dispose()

    def get_async_session(self) -> AsyncSession:
        """Get a database session."""
        return self.AsyncSessionLocal()


def extract_and_create_path_from_url(db_url: str) -> None:
    parsed = urlparse(db_url)
    file_path = parsed.path

    # Remove leading slashes for relative paths
    if file_path.startswith("/"):
        file_path = file_path[1:]

    # Determine the directory of the database file
    db_directory = Path(file_path).parent

    # Create the directory if it does not exist
    try:
        db_directory.mkdir(parents=True, exist_ok=True)
        logger.info("📁 Data directory exists or created")

    except Exception as e:
        print(f"⚠️ Failed to data create directory '{db_directory}': {e}")
        raise
