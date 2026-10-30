from src.schemas.base import BaseSchema
from annotated_types import Ge, MinLen, MaxLen
from typing import Annotated, Optional


class UserIn(BaseSchema):
    full_name: Annotated[str, MinLen(4), MaxLen(100)]
    email: Annotated[str, MinLen(10), MaxLen(255)]
    raw_password: Annotated[str, MinLen(8), MaxLen(255)]
    is_active: bool = False


class UserResponse(BaseSchema):
    id: Annotated[int, Ge(1)]
    full_name: Annotated[str, MinLen(4), MaxLen(100)]
    email: Annotated[str, MinLen(10), MaxLen(255)]
    is_active: bool


class UserUpdate(BaseSchema):
    full_name: Optional[Annotated[str, MinLen(4), MaxLen(100)]]
    email: Optional[Annotated[str, MinLen(10), MaxLen(255)]]
    is_active: Optional[bool]
