import logging


class CustomFormatter(logging.Formatter):
    """Custom formatter to shorten WARNING to WARN."""

    # def format(self, record):
    #     if record.levelname == 'WARNING':
    #         record.levelname = 'WARN'
    #     return super().format(record)


def setup_logging(log_level: str = "INFO") -> logging.Logger:
    """Configure logging based on settings."""
    handler = logging.StreamHandler()
    handler.setFormatter(
        CustomFormatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )

    logging.basicConfig(
        level=getattr(logging, log_level.upper()), handlers=[handler], force=True
    )
    return logging.getLogger(__name__)
