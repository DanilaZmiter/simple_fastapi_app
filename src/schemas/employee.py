from datetime import date, datetime
from typing import Annotated, Optional
from annotated_types import Ge, MaxLen

from src.schemas.base import BaseSchema


class EmployeeIn(BaseSchema):
    first_name: Annotated[str, MaxLen(40)]
    last_name: Annotated[str, MaxLen(40)]
    bio: Optional[str]


class EmployeeResponse(EmployeeIn):
    id: Annotated[int, Ge(1)]
    user_id: Annotated[int, Ge(1)]
    company_id: Annotated[int, Ge(1)]
    hired_at: date
    fired_at: date
    created_at: datetime
    updated_at: datetime


class EmployeeUpdate(BaseSchema):
    first_name: Optional[Annotated[str, MaxLen(40)]]
    last_name: Optional[Annotated[str, MaxLen(40)]]
    bio: Optional[str]
