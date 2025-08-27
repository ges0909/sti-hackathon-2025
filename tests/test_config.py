import pytest
from unittest.mock import patch
from config import Settings, settings


def test_settings_default_values():
    """Test Settings class default values."""
    test_settings = Settings()

    assert test_settings.database_url == "sqlite+aiosqlite:///./data/user.db"
    assert test_settings.log_level == "INFO"


def test_settings_from_env():
    """Test Settings class loading from environment."""
    with patch.dict(
        "os.environ",
        {"DATABASE_URL": "sqlite+aiosqlite:///test.db", "LOG_LEVEL": "DEBUG"},
    ):
        test_settings = Settings()

        assert test_settings.database_url == "sqlite+aiosqlite:///test.db"
        assert test_settings.log_level == "DEBUG"


def test_settings_instance():
    """Test global settings instance exists."""
    assert settings is not None
    assert isinstance(settings, Settings)
