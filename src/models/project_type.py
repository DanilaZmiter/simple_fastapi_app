from typing import TYPE_CHECKING

from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base import Base
from src.enums.project_types import (
    ProjectBusinessType,
    ProjectDifficulty,
    ProjectDirection,
    ProjectLifeCycle,
)

if TYPE_CHECKING:
    from src.models.project import ProjectORM


class ProjectTypeORM(Base):
    __tablename__ = "project_types_table"
    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects_table.id", ondelete="CASCADE"), primary_key=True
    )
    business_type: Mapped[ProjectBusinessType] = mapped_column(
        Enum(ProjectBusinessType)
    )
    direction_type: Mapped[ProjectDirection] = mapped_column(Enum(ProjectDirection))
    lifecycle_type: Mapped[ProjectLifeCycle] = mapped_column(Enum(ProjectLifeCycle))
    difficulty_type: Mapped[ProjectDifficulty] = mapped_column(Enum(ProjectDifficulty))
    project: Mapped["ProjectORM"] = relationship(back_populates="types")
