from datetime import date, datetime
from typing import Annotated, Optional
from annotated_types import Ge, MaxLen, MinLen

from src.schemas.base import BaseSchema


class EmployeeIn(BaseSchema):
    first_name: Annotated[str, MinLen(2), MaxLen(40)]
    last_name: Annotated[str, MinLen(2), MaxLen(40)]
    bio: Optional[Annotated[str, MaxLen(2000)]] = None


class EmployeeResponse(EmployeeIn):
    id: Annotated[int, Ge(1)]
    user_id: Annotated[int, Ge(1)]
    company_id: Annotated[int, Ge(1)]
    department_id: Optional[Annotated[int, Ge(1)]] = None
    hired_at: date
    fired_at: Optional[date] = None
    created_at: datetime
    updated_at: datetime


class EmployeeUpdate(BaseSchema):
    first_name: Optional[Annotated[str, MaxLen(40)]] = None
    last_name: Optional[Annotated[str, MaxLen(40)]] = None
    department_id: Optional[Annotated[int, Ge(1)]] = None
    bio: Optional[Annotated[str, MaxLen(2000)]] = None
