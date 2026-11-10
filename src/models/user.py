from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base import BaseORM

if TYPE_CHECKING:
    from src.models.employee import EmployeeORM


class UserORM(BaseORM):
    __tablename__ = "users_table"
    __table_args__ = (
        CheckConstraint(
            "length(email) > 9", name="check_email_lenght"
        ),  # check of email is grequal that 10
    )
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)

    employee: Mapped["EmployeeORM"] = relationship(back_populates="user")
