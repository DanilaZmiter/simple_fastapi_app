from enum import StrEnum


class TaskStatus(StrEnum):
    Todo = "Todo"
    In_progress = "In_progress"
    Review = "Review"
    Done = "Done"
    Cancelled = "Cancelled"


class TaskPriority(StrEnum):
    Low = "Low"
    Medium = "Medium"
    High = "High"
    Urgent = "Urgent"
