from typing import Annotated, Optional

from annotated_types import Ge, MaxLen
from pydantic import ConfigDict

from enums.company_types import CompanyTypes
from src.schemas.base import BaseSchema


class CompanyIn(BaseSchema):
    name: Annotated[str, MaxLen(120)]
    description: Annotated[str, MaxLen(1000)]
    type: CompanyTypes


class CompanyResponse(CompanyIn):
    model_config = ConfigDict(from_attributes=True)
    id: Annotated[int, Ge(1)]


class CompanyUpdate(BaseSchema):
    name: Optional[Annotated[str, MaxLen(120)]]
    description: Optional[Annotated[str, MaxLen(1000)]]
    type: Optional[CompanyTypes]
