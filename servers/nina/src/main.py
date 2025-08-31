import logging
import sys
from pathlib import Path
from typing import Dict, Any, List

import httpx
import yaml
from fastmcp import FastMCP

from ags_service import AgsService

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
    """Create MCP server from OpenAPI specification and adds AGS resource queries."""

    api_client = httpx.AsyncClient(base_url=base_url)
    mcp = FastMCP.from_openapi(openapi_spec=spec, client=api_client)
    # mcp = FastMCP.from_openapi(openapi_spec=spec, client=api_client, port=8000)

    @mcp.resource("ars://codes")
    async def get_ags_codes() -> List[Dict[str, str]]:
        """Returns all ARS codes with the name of their municipality."""
        ags_file = Path(__file__).parent.parent / "resources" / "GV100AD_31082025.txt"

        if not ags_file.exists():
            return []

        municipality_data = AgsService.parse_file(ags_file)

        return [
            {"municipality": municipality, "ars": ars}
            for municipality, ars in municipality_data.items()
        ]

    @mcp.resource("ars://codes/{municipality}")
    async def get_ags_code_by_municipality(municipality: str) -> str:
        """Get ARS code for a specific municipality name"""

        ags_file = Path(__file__).parent.parent / "resources" / "GV100AD_31082025.txt"

        if not ags_file.exists():
            return ""

        municipality_data = AgsService.parse_file(ags_file)

        # Search for municipality (case-insensitive)
        for municipality_name, ars_code in municipality_data.items():
            if municipality_name.lower() == municipality.lower():
                return ars_code  # Return immediately when found

        return ""  # Municipality not found

    @mcp.prompt("emergency-response")
    async def emergency_response_prompt(
        warning_type: str, severity: str = "medium"
    ) -> str:
        """Generate emergency response prompt."""
        return (
            f"Create emergency response plan for {warning_type} (severity: {severity})"
        )

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
