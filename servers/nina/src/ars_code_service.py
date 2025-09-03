from pathlib import Path
from typing import Dict


class ArsCodeService:
    RECORD_TYPE_START = 0
    RECORD_TYPE_END = 2
    ARS_START = 10
    ARS_END = 18
    MUNICIPALITY_START = 22
    MUNICIPALITY_END = 72
    MIN_LINE_LENGTH = 72

    TARGET_RECORD_TYPE = "60"

    @staticmethod
    def parse_file(file_path: str | Path) -> Dict[str, str]:
        """Parse AGS text file and extract municipality data.

        Returns dict with municipality name as key and ARS as value.
        """
        result: Dict[str, str] = {}

        if not file_path.exists():
            return {}

        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if (
                    len(line) >= ArsCodeService.MIN_LINE_LENGTH
                    and line[
                        ArsCodeService.RECORD_TYPE_START : ArsCodeService.RECORD_TYPE_END
                    ]
                    == ArsCodeService.TARGET_RECORD_TYPE
                ):
                    ars = line[
                        ArsCodeService.ARS_START : ArsCodeService.ARS_END
                    ].strip()
                    municipality = line[
                        ArsCodeService.MUNICIPALITY_START : ArsCodeService.MUNICIPALITY_END
                    ].strip()

                    if municipality:  # Only add if municipality name exists
                        result[municipality] = ars

        return result
