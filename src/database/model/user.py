from __future__ import annotations
from enum import Enum
from typing import TYPE_CHECKING

from database.model.base import Base
from sqlalchemy import String, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from database.model.address import Address


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    age: Mapped[int | None]
    gender: Mapped[Gender | None] = mapped_column(SQLEnum(Gender))

    address: Mapped[Address] = relationship(
        "Address", back_populates="user", uselist=False
    )
