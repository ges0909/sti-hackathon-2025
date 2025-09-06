from pathlib import Path
from typing import Dict

from nina.ars_code_service import ArsCodeService


def test_parse_ags_file():
    file_path = Path(__file__).parent.parent / "resources/GV100AD_31082025.txt"
    result: Dict[str, str] = ArsCodeService.parse_file(file_path)

    assert isinstance(result, dict)
    assert len(result) > 0
    assert "Blankenfelde-Mahlow" in result
    assert result["Blankenfelde-Mahlow"] == "12072017"
