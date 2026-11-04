from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.company import CompanyResponse, CompanyIn
from src.core.database import database
from src.repository.company import company_repo

router = APIRouter(prefix="/companies", tags=["Companies"])


@router.get("/list_all", response_model=List[CompanyResponse])
async def get_company_all(
    session: AsyncSession = Depends(database.get_scope_session), limit: int = 10
):
    response = await company_repo.get_list_company(session=session, limit=limit)
    return response


@router.get("/{company_id}", response_model=Optional[CompanyResponse])
async def get_company_by_id(
    company_id: int,
    session: AsyncSession = Depends(
        database.get_scope_session
    ),  # depends jsut take the session and use it inside fastapi
):
    response = await company_repo.get_company(
        session=session, id=company_id
    )  # take result of method to variable
    if response != None:
        return response  # check if object with such id is exist

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/create")
async def create_company(
    company_schema: CompanyIn,
    session: AsyncSession = Depends(database.get_scope_session),
):
    return company_repo.create_company(company_schema=company_schema, session=session)
