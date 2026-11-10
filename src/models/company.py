from typing import Optional

from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.enums.company_types import CompanyTypes
from src.models.base import BaseORM


class CompanyORM(BaseORM):
    __tablename__ = "companies_table"
    name: Mapped[str] = mapped_column(String(120))
    description: Mapped[Optional[str]] = mapped_column(String(1000))
    type: Mapped[CompanyTypes] = mapped_column(Enum(CompanyTypes))
    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users_table.id", ondelete="RESTRICT")
    )
