from datetime import datetime

from src.schemas.base import BaseSchema
from annotated_types import Ge, MinLen, MaxLen
from typing import Annotated, Optional
from pydantic import EmailStr


class UserIn(BaseSchema):
    email: Annotated[EmailStr, MinLen(10), MaxLen(255)]
    raw_password: Annotated[str, MinLen(8), MaxLen(255)]


class UserResponse(BaseSchema):
    id: Annotated[int, Ge(1)]
    email: Annotated[str, MinLen(10), MaxLen(255)]
    is_active: bool
    created_at: datetime
    updated_at: datetime


class UserUpdate(BaseSchema):
    email: Optional[Annotated[str, MinLen(10), MaxLen(255)]]
