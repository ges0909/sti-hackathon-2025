import logging

from .app import settings


def configure_logging():
    logging.basicConfig(
        level=settings.log_level,
        format="[%(asctime)s] %(levelname)-8s %(message)s",
        datefmt="%m/%d/%y %H:%M:%S",
        # Any previously configured loggers get reconfigured with the
        # timestamp format. This will make all log messages show the
        # date and time consistently.
        force=True,
    )
