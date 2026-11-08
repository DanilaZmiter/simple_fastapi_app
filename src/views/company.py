from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.company import CompanyORM
from src.schemas.company import CompanyResponse, CompanyIn, CompanyUpdate
from src.core.database import database
from src.repository.company import company_repo
from src.dependencies.company import cm_dependencies

router = APIRouter(prefix="/companies", tags=["Companies"])


@router.get("/list_all", response_model=List[CompanyResponse])
async def get_company_all(
    session: AsyncSession = Depends(database.get_scope_session), limit: int = 10
):
    response = await company_repo.get_list_company(session=session, limit=limit)
    return response


@router.get("/{company_id}", response_model=Optional[CompanyResponse])
async def get_company_by_id(
    company: CompanyORM = Depends(cm_dependencies.dget_company_by_id),
    session: AsyncSession = Depends(
        database.get_scope_session
    ),  # depends jsut take the session and use it inside fastapi
) -> Optional[CompanyResponse]:
    return CompanyResponse.model_validate(company)


@router.post("/create")
async def create_company(
    company_schema: CompanyIn,
    session: AsyncSession = Depends(database.get_scope_session),
):
    return await company_repo.create_company(
        company_schema=company_schema, session=session
    )


@router.patch("/update")
async def update_company(
    company_update: CompanyUpdate,
    company: CompanyORM = Depends(cm_dependencies.dget_company_by_id),
    session: AsyncSession = Depends(database.get_scope_session),
):
    return await company_repo.update_company(
        session=session, company_model=company, company_update=company_update
    )


@router.delete("/delete")
async def delete_company(
    company: CompanyORM = Depends(cm_dependencies.dget_company_by_id),
    session: AsyncSession = Depends(database.get_scope_session),
) -> None:
    await company_repo.delete_company(company_model=company, session=session)
