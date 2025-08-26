from database.models.base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    """Database model for a user."""

    __tablename__ = "users"

    # Option 1: Auto-increment (default)
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # Option 2: Identity column (PostgreSQL 10+, SQL Server)
    # id: Mapped[int] = mapped_column(Identity(start=1, increment=1), primary_key=True)

    # Option 3: Sequence (PostgreSQL, Oracle)
    # id: Mapped[int] = mapped_column(Sequence('user_id_seq'), primary_key=True)

    # Option 4: Manual control (no auto-generation)
    # id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)

    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    age: Mapped[int | None] = mapped_column(nullable=True)

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email}, age={self.age})>"
