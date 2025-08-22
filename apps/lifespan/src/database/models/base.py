from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy ORM models.

    It provides the basic declarative functionality. Models should inherit from this
    class to be automatically discovered by tools like `metadata.create_all`.
    """

    pass
