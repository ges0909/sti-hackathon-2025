from pydantic_settings import BaseSettings, SettingsConfigDict


# 'BaseSettings' adds env variable support
class Settings(BaseSettings):
    """Application settings."""

    database_url: str = None  # "sqlite+aiosqlite:///./data/user.db"
    log_level: str = "INFO"

    model_config = SettingsConfigDict(env_file="./.env")


# Singleton instance for the entire application
settings = Settings()
