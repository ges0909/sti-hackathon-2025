import logging
import sys
from pathlib import Path
from typing import Dict, Any

import httpx
import yaml
from fastmcp import FastMCP

from ars_code_service import ArsCodeService

BASE_URL = "https://warnung.bund.de/api31"
OPENAPI_SPEC_PATH = Path(__file__).parent.parent / "openapi.yaml"


def setup_logging() -> logging.Logger:
    """Configure logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger(__name__)


def load_openapi_spec(file_path: Path) -> Dict[str, Any]:
    """Load and parse OpenAPI specification from YAML file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"OpenAPI spec not found: {file_path}") from e
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML in {file_path}: {e}") from e


def create_mcp_server(spec: Dict[str, Any], base_url: str) -> FastMCP:
    """Create MCP server from OpenAPI spec and adds AGS resource queries."""

    api_client = httpx.AsyncClient(base_url=base_url)
    mcp = FastMCP.from_openapi(openapi_spec=spec, client=api_client)
    # mcp = FastMCP.from_openapi(openapi_spec=spec, client=api_client, port=8000)

    @mcp.resource(
        uri="ars://codes",
        name="amtliche_regionalschlüssel",
        description="Gibt alle Amtlichen Regionalschlüssel (ARS) zurück.",
        tags={"ARS"},
    )
    async def get_ars_codes() -> Dict[str, str]:
        """Returns all ARS codes with the name of their municipality."""
        gemeinde_verzeichnis = (
            Path(__file__).parent.parent / "resources" / "GV100AD_31082025.txt"
        )
        return ArsCodeService.parse_file(gemeinde_verzeichnis)

    @mcp.resource(
        uri="ars://codes/{gemeinde}",
        name="amtlicher_regionalschlüssel",
        description="Gibt den Amtlichen Regionalschlüssel (ARS) für eine Gemeinde zurück.",
        tags={"ARS"},
    )
    async def get_ars_code_by_municipality(gemeinde: str) -> str:
        """Get ARS code for a specific municipality name"""
        gemeinde_verzeichnis = (
            Path(__file__).parent.parent / "resources" / "GV100AD_31082025.txt"
        )
        ars_codes = ArsCodeService.parse_file(gemeinde_verzeichnis)
        # Search for a municipality (case-insensitive)
        for municipality_name, ars_code in ars_codes.items():
            if municipality_name.lower() == gemeinde.lower():
                return ars_code  # Return immediately when found

        return ""  # Municipality not found

    @mcp.prompt("mitarbeiter-notfall-warnungen-erstellen")
    async def emergency_response_prompt(country: str) -> str:
        """Generate emergency response prompt."""
        return f"""Prüfe auf Notfall-Warnungen für alle Mitarbeiter am Standort {country}!

    1. Ermittle alle Mitarbeiter in der Mitarbeiterdatenbank, die ihren Wohnsitz in Deutschland.
    2. Ermittle für jeden Wohnort den Amtliche Regionalschlüssel ARS mit Hilfe der Ressource @ars://codes/.
    3. Verwende den ARS um nach aktuellen Warnungen für die Wohnortgemeinde der Mitarbeite zu suchen.
    4. Geben den Namen des Mitarbeiters mit Adresse und amtlicher Warnung aus.
    """

    return mcp


def main() -> None:
    logger = setup_logging()

    try:
        logger.info("🚨 Starting NINA MCP Server...")

        # Load OpenAPI specification
        spec = load_openapi_spec(OPENAPI_SPEC_PATH)
        logger.info(f"✅ Loaded OpenAPI spec from {OPENAPI_SPEC_PATH}")

        # Create and run MCP server
        mcp = create_mcp_server(spec, BASE_URL)
        logger.info(f"✅ Created MCP server with base URL: {BASE_URL}")

        mcp.run()
        # mcp.run(transport="streamable-http")

    except Exception as e:
        logger.error(f"❌ Failed to start server: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
