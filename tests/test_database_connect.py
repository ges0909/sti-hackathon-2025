import pytest
from unittest.mock import patch, MagicMock, AsyncMock
from connect import Database


@pytest.mark.asyncio
async def test_database_connect():
    """Test Database.connect method."""
    with (
        patch("connect.create_async_engine") as mock_engine,
        patch("connect.async_sessionmaker") as mock_sessionmaker,
    ):
        mock_engine.return_value = MagicMock()
        mock_sessionmaker.return_value = MagicMock()

        db = await Database.connect()

        assert isinstance(db, Database)
        mock_engine.assert_called_once()
        mock_sessionmaker.assert_called_once()


@pytest.mark.asyncio
async def test_database_disconnect():
    """Test Database.disconnect method."""
    db = Database()
    mock_engine = MagicMock()
    mock_engine.dispose = AsyncMock()
    db.engine = mock_engine

    await db.disconnect()

    mock_engine.dispose.assert_called_once()


def test_get_async_session():
    """Test Database.get_async_session method."""
    db = Database()
    mock_session_local = MagicMock()
    db.async_session_local = mock_session_local

    session = db.get_async_session()

    mock_session_local.assert_called_once()
    assert session == mock_session_local.return_value
