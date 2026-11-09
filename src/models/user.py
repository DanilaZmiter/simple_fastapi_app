import datetime

from sqlalchemy import CheckConstraint, String, func
from sqlalchemy.orm import Mapped, mapped_column
from src.models.base import BaseORM
from datetime import datetime


class UserORM(BaseORM):
    __tablename__ = "users_table"
    __table_args__ = (
        CheckConstraint(
            "length(full_name) > 3", name="check_of_name_lenght"
        ),  # check of fullname is grequal that 4
        CheckConstraint(
            "length(email) > 9", name="check_of_email_lenght"
        ),  # check of email is grequal that 10
    )
    full_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str]
    is_active: Mapped[bool]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )
