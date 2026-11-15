from typing import TYPE_CHECKING, Optional

from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import BaseORM

if TYPE_CHECKING:
    from src.models.employee import EmployeeORM
    from src.models.project import ProjectORM


class ProjectMemberORM(BaseORM):
    __tablename__ = "project_members_table"
    __table_args__ = (
        UniqueConstraint("project_id", "employee_id", name="uq_project_member"),
    )

    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects_table.id", ondelete="CASCADE")
    )
    employee_id: Mapped[int] = mapped_column(
        ForeignKey("employees_table.id", ondelete="CASCADE")
    )
    role_in_project: Mapped[Optional[str]] = mapped_column(String(80), default=None)

    project: Mapped["ProjectORM"] = relationship(back_populates="members")
    employee: Mapped["EmployeeORM"] = relationship(back_populates="project_memberships")
