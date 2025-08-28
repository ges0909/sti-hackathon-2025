import logging
import sys

from config import settings
from server import mcp

logging.basicConfig(
    level=settings.log_level,
    format="[%(asctime)s] %(levelname)-8s %(message)s",
    datefmt="%m/%d/%y %H:%M:%S",
    # Any previously configured loggers get reconfigured with the
    # timestamp format. This will make all log messages show the
    # date and time consistently.
    force=True,
)

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
