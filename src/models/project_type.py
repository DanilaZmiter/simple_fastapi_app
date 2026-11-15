from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.models.base import Base
from src.enums.project_types import (
    ProjectTypesBusiness,
    ProjectTypesDifficulty,
    ProjectTypesDirection,
    ProjectTypesLifeCycle,
)


class ProjectType(Base):
    __tablename__ = "project_types_table"
    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects_table.id", ondelete="CASCADE"), primary_key=True
    )
    business_type: Mapped[ProjectTypesBusiness] = mapped_column(
        Enum(ProjectTypesBusiness)
    )
    direction_type: Mapped[ProjectTypesDirection] = mapped_column(
        Enum(ProjectTypesDirection)
    )
    lifecycle_type: Mapped[ProjectTypesLifeCycle] = mapped_column(
        Enum(ProjectTypesLifeCycle)
    )
    difficulty_type: Mapped[ProjectTypesDifficulty] = mapped_column(
        Enum(ProjectTypesDifficulty)
    )
