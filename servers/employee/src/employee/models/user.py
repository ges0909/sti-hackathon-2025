from __future__ import annotations
from enum import Enum
from typing import TYPE_CHECKING

from employee.models.base import Base
from sqlalchemy import Index, String, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from employee.models.address import Address
    from employee.models.work_status import WorkStatus


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

    address: Mapped[Address | None] = relationship(
        "Address", back_populates="user", uselist=False
    )
    work_status: Mapped[WorkStatus | None] = relationship(
        "WorkStatus", back_populates="user", uselist=False
    )

    __table_args__ = (
        Index("idx_user_email_lastname", "email", "last_name"),  # Composite index
    )
