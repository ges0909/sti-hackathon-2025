from __future__ import annotations

from typing import TYPE_CHECKING

from employee.models.base import Base
from sqlalchemy import Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from employee.models.user import User


class WorkStatus(Base):
    __tablename__ = "work_status"

    id: Mapped[int] = mapped_column(primary_key=True)
    is_home_office: Mapped[bool] = mapped_column(Boolean, default=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)

    user: Mapped[User] = relationship("User", back_populates="work_status")
