from .base import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Address(Base):
    """Database model for an address."""

    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    street: Mapped[str] = mapped_column(String(255))
    city: Mapped[str] = mapped_column(String(100))
    postal_code: Mapped[str] = mapped_column(String(20))
    country: Mapped[str] = mapped_column(String(100))

    # Foreign key to user
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    # Relationship back to user
    user: Mapped["User"] = relationship("User", back_populates="address")

    def __repr__(self):
        return f"<Address(street={self.street}, city={self.city}, postal_code={self.postal_code}, country={self.country})>"
