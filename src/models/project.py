from datetime import date
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Enum, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums.project_types import ProjectStatus
from src.models.base import BaseORM

if TYPE_CHECKING:
    from src.models.company import CompanyORM
    from src.models.employee import EmployeeORM
    from src.models.project_type import ProjectTypeORM
    from src.models.project_member import ProjectMemberORM

    # from src.models.task import TaskORM


class ProjectORM(BaseORM):
    __tablename__ = "projects_table"

    name: Mapped[str] = mapped_column(String(200))
    description: Mapped[Optional[str]] = mapped_column(Text, default=None)
    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies_table.id", ondelete="CASCADE"), index=True
    )
    status: Mapped[ProjectStatus] = mapped_column(
        Enum(ProjectStatus), default=ProjectStatus.Draft
    )
    manager_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("employees_table.id", ondelete="SET NULL")
    )
    start_date: Mapped[Optional[date]] = mapped_column(default=None)
    end_date: Mapped[Optional[date]] = mapped_column(default=None)

    company: Mapped["CompanyORM"] = relationship(back_populates="projects")
    manager: Mapped[Optional["EmployeeORM"]] = relationship(
        foreign_keys=[manager_id], back_populates="managed_projects"
    )
    types: Mapped[Optional["ProjectTypeORM"]] = relationship(
        back_populates="project", uselist=False
    )
    members: Mapped[List["ProjectMemberORM"]] = relationship(back_populates="project")
    # tasks: Mapped[List["TaskORM"]] = relationship(back_populates="project")
