import logging
from server import mcp

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    logger.info("🚨 NINA MCP Server starts...")
    mcp.run()


if __name__ == "__main__":
    main()
