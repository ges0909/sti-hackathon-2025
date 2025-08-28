import logging
import sys

from config.log import configure_logging
from server import mcp

configure_logging()
logger = logging.getLogger(__name__)


def main():
    logger.info("🚀 MCP Server starting...")
    try:
        mcp.run()
    except Exception as e:
        if "UnicodeDecodeError" in str(e) or "ExceptionGroup" in type(e).__name__:
            logger.info("✅ MCP Server shutdown complete")
            sys.exit(0)
        raise


if __name__ == "__main__":
    main()
