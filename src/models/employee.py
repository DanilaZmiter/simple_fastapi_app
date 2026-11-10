from datetime import date
from typing import TYPE_CHECKING, Optional

from sqlalchemy import Enum, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.enums.employee_roles import EmployeeRoles
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
    role: Mapped[EmployeeRoles] = mapped_column(
        Enum(EmployeeRoles), default=EmployeeRoles.Employee
    )
    hired_at: Mapped[date] = mapped_column(
        default=date.today, server_default=func.current_date()
    )
    fired_at: Mapped[Optional[date]]

    user: Mapped["UserORM"] = relationship(
        foreign_keys=[user_id], back_populates="employee"
    )
    company: Mapped["CompanyORM"] = relationship(
        foreign_keys=[company_id], back_populates="employees"
    )
    department: Mapped[Optional["DepartmentORM"]] = relationship(
        foreign_keys=[department_id], back_populates="employees"
    )
