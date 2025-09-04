import logging
import sys
from pathlib import Path

import yaml
from server import create_server

BASE_URL = "https://warnung.bund.de/api31"
OPENAPI_SPEC_PATH = Path(__file__).parent.parent / "openapi.yaml"

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

with open(OPENAPI_SPEC_PATH, "r", encoding="utf-8") as f:
    spec = yaml.safe_load(f)
mcp = create_server(spec, BASE_URL)


def main() -> None:
    try:
        logger.info("🚨 Starting NINA MCP Server...")
        mcp.run()
    except Exception as e:
        logger.error(f"❌ Failed to start server: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
