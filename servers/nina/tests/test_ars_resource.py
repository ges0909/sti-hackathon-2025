import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from ars_code_service import ArsCodeService

GEMEINDE_FILE = Path(__file__).parent.parent / "resources" / "GV100AD_31082025.txt"


def test_ars_codes_loading():
    """Test ARS codes load"""
    codes = ArsCodeService.parse_file(GEMEINDE_FILE)
    assert isinstance(codes, dict)
    assert len(codes) > 0
    assert all(isinstance(k, str) and isinstance(v, str) for k, v in codes.items())


def test_ars_code_lookup():
    """Test specific municipality lookup"""
    codes = ArsCodeService.parse_file(GEMEINDE_FILE)

    # Test case-insensitive search
    found = False
    for name, code in codes.items():
        if "münchen" in name.lower():
            assert code.startswith("09")
            found = True
            break

    if not found and codes:
        first_name, first_code = next(iter(codes.items()))
        assert len(first_code) >= 8  # ARS codes have at least 8 digits


def test_file_exists():
    """Test that the gemeinde file exists"""
    assert GEMEINDE_FILE.exists(), f"File not found: {GEMEINDE_FILE}"
