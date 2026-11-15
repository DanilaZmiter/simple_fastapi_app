from enum import StrEnum


class ProjectBusinessType(StrEnum):
    Production = "Production"
    Internal = "Internal"
    Custom = "Custom"


class ProjectDirection(StrEnum):
    SoftwareDevelopment = "Software Development"
    InfrastructureAndDevOPS = "Infrastructure and DevOps"
    DataAIML = "Data/AI/ML"
    Integration = "Integration"
    InfoSec = "InfoSec"


class ProjectLifeCycle(StrEnum):
    Greenfield = "Greenfield"
    Brownfield = "Brownfield"
    MigrationRefactoring = "Migration/Refactoring"
    Support = "Support"


class ProjectDifficulty(StrEnum):
    Predictable = "Predictable"
    Complex = "Complex"
    RandD = "R&D"


class ProjectStatus(StrEnum):
    Draft = "Draft"
    Active = "Active"
    OnHold = "On_hold"
    Completed = "Completed"
    Archived = "Archived"
