from pathlib import Path

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    project_root: Path = Path(__file__).parent.parent.parent.parent
    default_database_url: str = "sqlite+aiosqlite:///" + str(
        project_root / "data" / "mitarbeiter.db"
    )

    database_url: str = Field(default=default_database_url)
    log_level: str = Field(default="INFO")
    initial_users_count: int = Field(default=10)

    model_config = SettingsConfigDict(env_file="./.env")

    @field_validator("database_url")
    @classmethod
    def validate_database_url(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("DATABASE_URL must be set and non-empty")
        return value

    @field_validator("log_level")
    @classmethod
    def validate_log_level(cls, value: str) -> str:
        valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
        upper_value = value.upper()
        if upper_value not in valid_levels:
            raise ValueError(f"LOG_LEVEL must be one of: {valid_levels}")
        return upper_value

    @field_validator("initial_users_count")
    @classmethod
    def validate_initial_users_count(cls, value: int) -> int:
        if not 0 <= value <= 1000:
            raise ValueError("INITIAL_USERS_COUNT must be between 0 and 1000")
        return value


settings = Settings()
