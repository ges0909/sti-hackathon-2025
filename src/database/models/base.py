from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy ORM models.

    Models should inherit from this class to be automatically discovered by
    mcp_tools like `metadata.create_all`.
    """

    pass
