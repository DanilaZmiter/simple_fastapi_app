from typing import Any, List, Optional

from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession
from models.company import CompanyORM
from schemas.user import UserIn, UserResponse
from src.schemas.company import CompanyResponse


class CompanyRepository:  # by class for future upgrades
    """Read methods for repository"""

    @classmethod
    async def get_company(
        cls, session: AsyncSession, id: int
    ) -> Optional[CompanyResponse]:
        result: Optional[CompanyORM] = await session.get(
            CompanyORM, id
        )  # get company model object
        return CompanyResponse.model_validate(
            result
        )  # return pydantic schema for json response from view methods

    @classmethod
    async def get_list_company(
        cls, session: AsyncSession, limit: int
    ) -> List[CompanyResponse]:
        stmt = (
            select(CompanyORM).order_by(CompanyORM.id).limit(limit=limit)
        )  # order_by - sorting, limit - pagination
        result: Result[Any] = await session.execute(stmt)
        return list(result.scalars().all())  # scalars used to get elements from tuple

    """Create methods of repository"""

    @classmethod
    async def create_company(
        cls, user_schema: UserIn, session: AsyncSession
    ) -> UserResponse:
        orm_model: CompanyORM = CompanyORM(**user_schema.model_dump())
        session.add(orm_model)  # add our company to database
        await session.commit()  # stage changes of database
        await session.refresh(orm_model)  # update model in database
        return UserResponse.model_validate(
            orm_model
        )  # take new model with id to server response


company_repo = CompanyRepository()
