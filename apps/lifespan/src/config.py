from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    database_url: str = "sqlite+aiosqlite:///../data/user.db"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
