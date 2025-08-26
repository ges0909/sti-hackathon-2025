import logging
import sys

from config import settings
from server import mcp
from logger import setup_logging

# Setup logging
logger = setup_logging(settings.log_level)

# Suppress SQLAlchemy connection termination errors
logging.getLogger("sqlalchemy.pool").setLevel(logging.CRITICAL)
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)


def main():
    logger.info("🚀 MCP Server starting...")
    try:
        mcp.run()
    except Exception as e:
        if "UnicodeDecodeError" in str(e) or "ExceptionGroup" in str(type(e).__name__):
            logger.info("✅ MCP Server shutdown complete")
            sys.exit(0)
        raise


if __name__ == "__main__":
    main()
