import logging
from functools import lru_cache
from pathlib import Path
from typing import Dict

import httpx
import yaml
from fastmcp import FastMCP

from nina.ars_code_service import ArsCodeService

logger = logging.getLogger(__name__)

BASE_URL = "https://warnung.bund.de/api31"
OPENAPI_SPEC_PATH = Path(__file__).parent.parent.parent / "openapi.yaml"
GEMEINDE_FILE = Path(__file__).parent.parent / "resources" / "GV100AD_31082025.txt"

with open(OPENAPI_SPEC_PATH, "r", encoding="utf-8") as f:
    openapi_spec = yaml.safe_load(f)

mcp = FastMCP.from_openapi(
    openapi_spec=openapi_spec, client=httpx.AsyncClient(base_url=BASE_URL)
)


@mcp.resource(
    uri="ars://codes",
    name="amtliche_regionalschlüssel",
    description="Gibt alle Amtlichen Regionalschlüssel (ARS) zurück.",
    tags={"ARS"},
)
async def get_ars_codes() -> Dict[str, str]:
    return _get_ars_codes()


@mcp.resource(
    uri="ars://codes/{gemeinde}",
    name="amtlicher_regionalschlüssel",
    description="Gibt den Amtlichen Regionalschlüssel (ARS) für eine Gemeinde zurück.",
    tags={"ARS"},
)
async def get_ars_code_by_municipality(gemeinde: str) -> str:
    codes = _get_ars_codes()
    for name, code in codes.items():
        if name.lower() == gemeinde.lower():
            return code
    return ""


@mcp.prompt(name="ars_lookup", description="ARS-Codes nachschlagen")
async def ars_lookup_prompt(query: str = "") -> str:
    return f"""WICHTIGE ANWEISUNG FÜR GEMINI:

Du hast Zugriff auf eine MCP-Ressource mit der URI: ars://codes

Diese Ressource enthält alle deutschen Amtlichen Regionalschlüssel.

VERWENDE AUSSCHLIESSLICH DIESE RESSOURCE - keine Websuche!

Schritte:
1. Lade die MCP-Ressource ars://codes
2. Suche in den Daten nach: {query}
3. Gib die Ergebnisse aus

Beginne JETZT mit dem Laden der Ressource ars://codes"""


@mcp.prompt("zeige-notfall-warnungen")
async def emergency_response_prompt(country: str) -> str:
    return f"""Prüfe auf Notfall-Warnungen für alle Mitarbeiter am Standort {country}!

DATENQUELLE:
- Verwende ausschließlich die MCP-Ressource "ars://codes"
- KEINE Websuche für ARS-Codes oder Gemeindedaten!

1. Ermittle alle Mitarbeiter aus der Mitarbeiterdatenbank, die ihren Wohnsitz
   in Deutschland haben.
2. Ermittle für jeden Wohnort den Amtliche Regionalschlüssel ARS.
3. Suche mit dem ARS nach aktuellen Warnungen mit der NINA API.
4. Geben den Namen des Mitarbeiters mit Adresse und amtlicher Warnung aus.
"""


@lru_cache(maxsize=1)
def _get_ars_codes() -> Dict[str, str]:
    try:
        logger.debug("ARS-Codes werden geladen...")
        codes = ArsCodeService.parse_file(GEMEINDE_FILE)
        logger.info(f"{len(codes)} ARS-Codes erfolgreich geladen")
        return codes
    except FileNotFoundError as e:
        raise RuntimeError(f"Gemeinde-Datei nicht gefunden: {GEMEINDE_FILE}") from e
    except Exception as e:
        raise RuntimeError(f"Fehler beim Parsen der ARS-Codes: {str(e)}") from e
