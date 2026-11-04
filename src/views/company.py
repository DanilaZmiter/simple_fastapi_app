from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.company import CompanyResponse
from src.core.database import database
from src.repository.company import company_repo

router = APIRouter(prefix="/companies", tags=["Companies"])


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
