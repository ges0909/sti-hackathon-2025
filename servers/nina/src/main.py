import logging
import sys
from pathlib import Path
from typing import Dict, Any

import httpx
import yaml
from fastmcp import FastMCP

# Configuration
BASE_URL = "https://warnung.bund.de/api31"
OPENAPI_SPEC_PATH = Path("openapi.yaml")


def setup_logging() -> logging.Logger:
    """Configure logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
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
    """Create MCP server from OpenAPI specification."""
    api_client = httpx.AsyncClient(base_url=base_url)
    return FastMCP.from_openapi(openapi_spec=spec, client=api_client)


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

    except Exception as e:
        logger.error(f"❌ Failed to start server: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
