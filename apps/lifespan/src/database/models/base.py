from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Abstract basic class for all database models"""

    __abstract__ = True
