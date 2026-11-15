from datetime import date
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Enum, ForeignKey, Index, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.enums.task_types import TaskPriority, TaskStatus
from src.models.base import BaseORM

if TYPE_CHECKING:
    from src.models.employee import EmployeeORM
    from src.models.project import ProjectORM


class TaskORM(BaseORM):
    __tablename__ = "tasks_table"
    __table_args__ = (Index("ix_task_project_status", "project_id", "status"),)

    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects_table.id", ondelete="CASCADE")
    )
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[Optional[str]] = mapped_column(Text, default=None)
    status: Mapped[TaskStatus] = mapped_column(
        Enum(TaskStatus), default=TaskStatus.Todo
    )
    priority: Mapped[TaskPriority] = mapped_column(
        Enum(TaskPriority), default=TaskPriority.Medium
    )
    assignee_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("employees_table.id", ondelete="SET NULL")
    )
    author_id: Mapped[int] = mapped_column(
        ForeignKey("employees_table.id", ondelete="RESTRICT")
    )
    parent_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("tasks_table.id", ondelete="CASCADE")
    )
    due_date: Mapped[Optional[date]] = mapped_column(default=None)

    project: Mapped["ProjectORM"] = relationship(back_populates="tasks")
    assignee: Mapped[Optional["EmployeeORM"]] = relationship(
        foreign_keys=[assignee_id], back_populates="assigned_tasks"
    )
    author: Mapped["EmployeeORM"] = relationship(
        foreign_keys=[author_id], back_populates="authored_tasks"
    )
    parent: Mapped[Optional["TaskORM"]] = relationship(
        remote_side="TaskORM.id", back_populates="subtasks"
    )
    subtasks: Mapped[List["TaskORM"]] = relationship(back_populates="parent")
