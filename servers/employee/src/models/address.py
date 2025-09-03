from __future__ import annotations

from typing import TYPE_CHECKING

from models.base import Base
from sqlalchemy import String, ForeignKey, event
from sqlalchemy.orm import Mapped, mapped_column, relationship
import pycountry

if TYPE_CHECKING:
    from models.user import User


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True)
    street: Mapped[str] = mapped_column(String(255))
    city: Mapped[str] = mapped_column(String(100))
    postal_code: Mapped[str] = mapped_column(String(20))
    country_code: Mapped[str] = mapped_column(String(2))  # ISO 3166-1 alpha-2
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped[User] = relationship("User", back_populates="address")


@event.listens_for(Address.country_code, "set")
def validate_country_code(target, value, old_value, initiator):
    """Validate ISO 3166-1 alpha-2 country code."""
    if value is not None and not pycountry.countries.get(alpha_2=value.upper()):
        raise ValueError(
            f"Invalid country code '{value}'. Must be ISO 3166-1 alpha-2 format (e.g., 'DE', 'US', 'FR')."
        )
    return value.upper() if value else value
