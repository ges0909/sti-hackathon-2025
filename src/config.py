from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    database_url: str = Field(default="", description="Database URL is required")
    log_level: str = Field(default="INFO", description="Logging level")
    initial_users_count: int = Field(default=10, description="Number of initial users to create")

    # Add env variable support
    model_config = SettingsConfigDict(env_file="./.env")

    @classmethod
    @field_validator("database_url")
    def validate_database_url(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("DATABASE_URL must be set and non-empty")
        return value

    @classmethod
    @field_validator("log_level")
    def validate_log_level(cls, value: str) -> str:
        valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
        if value.upper() not in valid_levels:
            raise ValueError(f"LOG_LEVEL must be one of: {valid_levels}")
        return value.upper()

    @classmethod
    @field_validator("initial_users_count")
    def validate_initial_users_count(cls, value: int) -> int:
        if value < 0 or value > 1000:
            raise ValueError("INITIAL_USERS_COUNT must be between 0 and 1000")
        return value


# Singleton instance for the entire application
settings = Settings()
