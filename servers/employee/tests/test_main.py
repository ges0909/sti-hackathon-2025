import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import pytest
from unittest.mock import patch
from main import main


def test_main_success():
    """Test main function successful execution."""
    with patch("main.mcp") as mock_mcp:
        mock_mcp.run.return_value = None

        main()

        mock_mcp.run.assert_called_once()


def test_main_other_exception():
    """Test main function with other exceptions."""
    with patch("main.mcp") as mock_mcp:
        mock_mcp.run.side_effect = ValueError("Other error")

        with pytest.raises(ValueError, match="Other error"):
            main()


def test_main_entry_point():
    """Test main entry point execution."""
    with patch("main.main") as mock_main_func, patch("__main__.__name__", "__main__"):
        mock_main_func()
        mock_main_func.assert_called_once()
