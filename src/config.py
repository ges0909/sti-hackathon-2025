from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    database_url: str = Field(default="", description="Database URL is required")
    log_level: str = Field(default="INFO", description="Logging level")

    # Add env variable support
    model_config = SettingsConfigDict(env_file="./.env")

    @field_validator("database_url")
    @classmethod
    def validate_database_url(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("DATABASE_URL must be set and non-empty")
        return value

    @field_validator("log_level")
    @classmethod
    def validate_log_level(cls, value: str) -> str:
        valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
        if value.upper() not in valid_levels:
            raise ValueError(f"LOG_LEVEL must be one of: {valid_levels}")
        return value.upper()


# Singleton instance for the entire application
settings = Settings()
