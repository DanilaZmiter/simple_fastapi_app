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


class EmployeeUpdate(BaseSchema):
    first_name: Optional[Annotated[str, MaxLen(40)]]
    last_name: Optional[Annotated[str, MaxLen(40)]]
    bio: Optional[str]
