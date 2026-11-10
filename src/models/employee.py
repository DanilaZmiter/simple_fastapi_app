from datetime import date
from typing import TYPE_CHECKING, Optional

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import BaseORM

if TYPE_CHECKING:
    from src.models.user import UserORM
    from src.models.company import CompanyORM
    from src.models.department import DepartmentORM


class EmployeeORM(BaseORM):
    __tablename__ = "employees_table"
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users_table.id", ondelete="CASCADE"), unique=True
    )
    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies_table.id", ondelete="CASCADE")
    )
    department_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("departments_table.id", ondelete="SET NULL")
    )
    first_name: Mapped[str] = mapped_column(String(40))
    last_name: Mapped[str] = mapped_column(String(40))
    bio: Mapped[Optional[str]] = mapped_column(Text)
    hired_at: Mapped[date] = mapped_column(default=date.today)
    fired_at: Mapped[Optional[date]]

    user: Mapped["UserORM"] = relationship(back_populates="employee")
    company: Mapped["CompanyORM"] = relationship(back_populates="employees")
    department: Mapped["DepartmentORM"] = relationship(foreign_keys=[department_id])
