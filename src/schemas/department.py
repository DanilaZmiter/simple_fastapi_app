from datetime import datetime
from typing import Annotated, Optional

from annotated_types import Ge, MaxLen

from src.schemas.base import BaseSchema


class DepartmentIn(BaseSchema):
    name: Annotated[str, MaxLen(120)]


class DepartmentResponse(DepartmentIn):
    id: Annotated[int, Ge(1)]
    company_id: Annotated[int, Ge(1)]
    parent_id: Annotated[int, Ge(1)]
    created_at: datetime
    updated_at: datetime


class DepartmentUpdate(BaseSchema):
    name: Optional[Annotated[str, MaxLen(120)]]
