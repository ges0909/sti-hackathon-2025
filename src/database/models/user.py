from database.models.base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    """Database model for a user."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    age: Mapped[int | None] = mapped_column(nullable=True)

    # Relationship to address (one-to-one)
    address: Mapped["Address"] = relationship(
        "Address", back_populates="user", uselist=False
    )

    def __repr__(self):
        return f"<User(first_name={self.first_name}, last_name={self.last_name}, email={self.email}, age={self.age})>"
