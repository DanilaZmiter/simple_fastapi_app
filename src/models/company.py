from typing import TYPE_CHECKING, Optional

from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums.company_types import CompanyTypes
from src.models.base import BaseORM

if TYPE_CHECKING:
    from src.models.user import UserORM
    from src.models.employee import EmployeeORM


class CompanyORM(BaseORM):
    __tablename__ = "companies_table"
    name: Mapped[str] = mapped_column(String(120))
    description: Mapped[Optional[str]] = mapped_column(String(1000))
    type: Mapped[CompanyTypes] = mapped_column(Enum(CompanyTypes))
    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users_table.id", ondelete="RESTRICT")
    )

    owner: Mapped["UserORM"] = relationship(foreign_keys=[owner_id])
    employees: Mapped["EmployeeORM"] = relationship(back_populates="company")
