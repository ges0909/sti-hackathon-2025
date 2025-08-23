from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database.models.base import Base


class User(Base):
    """Database model for a user."""

    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    age: Mapped[int | None] = mapped_column(nullable=True)

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email}, age={self.age})>"
