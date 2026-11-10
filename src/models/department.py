from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import BaseORM

if TYPE_CHECKING:
    from src.models.company import CompanyORM
    from src.models.employee import EmployeeORM


class DepartmentORM(BaseORM):
    __tablename__ = "departments_table"
    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies_table.id", ondelete="CASCADE"), index=True
    )
    name: Mapped[str] = mapped_column(String(120))
    parent_id: Optional[Mapped[int]] = mapped_column(
        ForeignKey("departments_table.id", ondelete="SET NULL")
    )

    parent: Mapped[Optional["DepartmentORM"]] = relationship(
        remote_side="DepartmentORM.id", back_populates="children"
    )
    children: Mapped[Optional[List["DepartmentORM"]]] = relationship(
        back_populates="parent"
    )
    company: Mapped["CompanyORM"] = relationship(back_populates="departments")
    employees: Mapped[List["EmployeeORM"]] = relationship(back_populates="department")
