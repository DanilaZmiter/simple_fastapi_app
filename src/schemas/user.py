from src.schemas.base import BaseSchema
from annotated_types import MinLen, MaxLen
from typing import Annotated


class UserIn(BaseSchema):
    full_name: Annotated[str, MinLen(4), MaxLen(100)]
    email: Annotated[str, MinLen(10), MaxLen(255)]
    raw_password: Annotated[str, MinLen(8), MaxLen(255)]
    is_active: bool = False
