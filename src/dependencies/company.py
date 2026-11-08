from typing import Annotated, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, Path, status

from src.core.database import database
from src.models.company import CompanyORM
from src.repository.company import company_repo


class CompanyDependincies:
    @classmethod
    async def dget_company_by_id(
        cls,
        company_id: Annotated[int, Path],  # Path to make it query parameter
        session: AsyncSession = Depends(database.get_scope_session),
    ) -> Optional[CompanyORM]:
        company = await company_repo.get_company(session=session, id=company_id)
        if company:
            return company
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


cm_dependencies = CompanyDependincies()
