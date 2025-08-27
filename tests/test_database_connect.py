import pytest
import pytest_asyncio
from unittest.mock import patch, MagicMock
from pathlib import Path
from database.connect import Database, extract_and_create_path_from_url


@pytest.mark.asyncio
async def test_database_connect():
    """Test Database.connect method."""
    with patch('database.connect.create_async_engine') as mock_engine, \
         patch('database.connect.async_sessionmaker') as mock_sessionmaker, \
         patch('database.connect.extract_and_create_path_from_url'):
        
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


def test_extract_and_create_path_from_url_sqlite():
    """Test path extraction for SQLite URL."""
    with patch('database.connect.Path') as mock_path:
        mock_path_instance = MagicMock()
        mock_path.return_value = mock_path_instance
        mock_path_instance.parent = MagicMock()
        
        extract_and_create_path_from_url("sqlite:///data/test.db")
        
        mock_path_instance.parent.mkdir.assert_called_once_with(parents=True, exist_ok=True)


def test_extract_and_create_path_from_url_memory():
    """Test path extraction for in-memory database."""
    with patch('database.connect.Path') as mock_path:
        mock_path_instance = MagicMock()
        mock_path.return_value = mock_path_instance
        mock_path_instance.parent = MagicMock()
        
        extract_and_create_path_from_url("sqlite:///:memory:")
        
        mock_path_instance.parent.mkdir.assert_called_once_with(parents=True, exist_ok=True)


def test_extract_and_create_path_mkdir_exception():
    """Test path creation with exception."""
    with patch('database.connect.Path') as mock_path:
        mock_path_instance = MagicMock()
        mock_path.return_value = mock_path_instance
        mock_path_instance.parent.mkdir.side_effect = Exception("Permission denied")
        
        with pytest.raises(Exception, match="Permission denied"):
            extract_and_create_path_from_url("sqlite:///data/test.db")