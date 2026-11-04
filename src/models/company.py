from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from src.enums.company_types import CompanyTypes
from src.models.base import BaseORM


class CompanyORM(BaseORM):
    __tablename__ = "companies_table"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120))
    description: Mapped[str] = mapped_column(String(1000))
    type: Mapped[CompanyTypes] = mapped_column(Enum(CompanyTypes))
