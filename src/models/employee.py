from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import BaseORM

if TYPE_CHECKING:
    from src.models.user import UserORM


class EmployeeORM(BaseORM):
    __tablename__ = "employees_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users_table.id", ondelete="CASCADE")
    )
    company_id: Mapped[int] = mapped_column(ForeignKey("companies_table.id"))
    first_name: Mapped[str] = mapped_column(String(40))
    last_name: Mapped[str] = mapped_column(String(40))
    bio: Mapped[str] = mapped_column(Text)
    hired_at: Mapped[date] = mapped_column(default=date.today)
    fired_at: Mapped[date]

    user: Mapped["UserORM"] = relationship(back_populates="employee")
