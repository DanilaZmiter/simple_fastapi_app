from datetime import datetime
from typing import Annotated, Optional

from annotated_types import Ge, MaxLen, MinLen

from src.schemas.base import BaseSchema


class DepartmentIn(BaseSchema):
    name: Annotated[str, MinLen(1), MaxLen(120)]
    parent_id: Optional[Annotated[int, Ge(1)]] = None


class DepartmentResponse(DepartmentIn):
    id: Annotated[int, Ge(1)]
    company_id: Annotated[int, Ge(1)]
    created_at: datetime
    updated_at: datetime


class DepartmentUpdate(BaseSchema):
    name: Optional[Annotated[str, MinLen(1), MaxLen(120)]] = None
    parent_id: Optional[Annotated[int, Ge(1)]] = None
