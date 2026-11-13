from datetime import datetime
from typing import Annotated, Optional

from annotated_types import Ge, MaxLen, MinLen

from src.enums.company_types import CompanyTypes
from src.schemas.base import BaseSchema


class CompanyIn(BaseSchema):
    name: Annotated[str, MinLen(3), MaxLen(120)]
    description: Optional[Annotated[str, MaxLen(1000)]]
    type: CompanyTypes


class CompanyResponse(CompanyIn):
    id: Annotated[int, Ge(1)]
    created_at: datetime
    updated_at: datetime


class CompanyUpdate(BaseSchema):
    name: Optional[Annotated[str, MinLen(3), MaxLen(120)]]
    description: Optional[Annotated[str, MaxLen(1000)]]
    type: Optional[CompanyTypes]
