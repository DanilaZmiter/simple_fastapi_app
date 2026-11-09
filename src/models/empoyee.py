from tkinter import CASCADE
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import BaseORM

if TYPE_CHECKING:
    from src.models.user import UserORM
    from src.models.company import CompanyORM


class EmployeeORM(BaseORM):
    __tablename__ = "employee_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id", ondelete=CASCADE))
    company_id: Mapped[int] = mapped_column(ForeignKey("companies_table.id"))
    first_name: Mapped[str] = mapped_column(String(40))
    last_name: Mapped[str] = mapped_column(String(40))
    bio: Mapped[str] = mapped_column(Text)

    user: Mapped["UserORM"] = relationship(back_populates="employee_profile")
    company: Mapped["CompanyORM"] = relationship(back_populates="employee_profiles")
