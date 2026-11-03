from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from models.company import CompanyORM
from src.schemas.company import CompanyResponse


class CompanyRepository:  # by class for future upgrades
    """Read methods for repository"""

    @classmethod
    async def get_company(cls, session: AsyncSession, id: int) -> CompanyResponse:
        result: Optional[CompanyORM] = await session.get(
            CompanyORM, id
        )  # get company model object
        return CompanyResponse.model_validate(
            result
        )  # return pydantic schema for json response from view methods


company_repo = CompanyRepository()
