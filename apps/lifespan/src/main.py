import sys
import logging
from server import mcp

# Suppress SQLAlchemy connection termination errors
logging.getLogger("sqlalchemy.pool").setLevel(logging.CRITICAL)
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)


def main():
    print("🚀 MCP Server starting...", file=sys.stderr)
    try:
        mcp.run()
    except Exception as e:
        if "UnicodeDecodeError" in str(e) or "ExceptionGroup" in str(type(e).__name__):
            print("👋 MCP Server shutdown complete", file=sys.stderr)
            sys.exit(0)
        raise


if __name__ == "__main__":
    main()
