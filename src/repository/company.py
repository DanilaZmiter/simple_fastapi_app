from typing import Any, List, Optional

from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.company import CompanyORM
from src.schemas.company import CompanyIn, CompanyResponse, CompanyUpdate


class CompanyRepository:  # by class for future upgrades
    """Read methods for repository"""

    @classmethod
    async def get_company(cls, session: AsyncSession, id: int) -> Optional[CompanyORM]:
        result: Optional[CompanyORM] = await session.get(
            CompanyORM, id
        )  # get company model object
        if result != None:
            return result  # return model for dependency layer
        return None

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
        cls, company_schema: CompanyIn, session: AsyncSession
    ) -> CompanyResponse:
        orm_model: CompanyORM = CompanyORM(**company_schema.model_dump())
        session.add(orm_model)  # add our company to database
        await session.commit()  # stage changes of database
        await session.refresh(orm_model)  # update model in database
        return CompanyResponse.model_validate(
            orm_model
        )  # take new model with id to server response

    @classmethod
    async def update_company(
        cls,
        company_model: CompanyORM,
        company_update: CompanyUpdate,
        session: AsyncSession,
    ) -> CompanyResponse:
        for name, value in company_update.model_dump(
            exclude_none=True
        ).items():  # add only not None elements
            setattr(company_model, name, value)
        await session.commit()
        return CompanyResponse.model_validate(company_model)

    @classmethod
    async def delete_company(
        cls, company_model: CompanyORM, session: AsyncSession
    ) -> None:
        await session.delete(company_model)


company_repo = CompanyRepository()
