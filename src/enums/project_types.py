from enum import StrEnum


class ProjectTypesBusiness(StrEnum):
    Production = "Production"
    Internal = "Internal"
    Custom = "Custom"


class ProjectTypesDirection(StrEnum):
    SoftwareDevelopment = "Software Development"
    InfrastructureAndDevOPS = "Infrastructure and DevOps"
    DataAIML = "Data/AI/ML"
    Integration = "Integration"
    InfoSec = "InfoSec"


class ProjectTypesLifeCycle(StrEnum):
    Greenfield = "Greenfield"
    Brownfield = "Brownfield"
    MigrationRefactoring = "Migration/Refactoring"
    Support = "Support"


class ProjectTypesDifficulty(StrEnum):
    Predictable = "Predictable"
    Complex = "Complex"
    RandD = "R&D"


class ProjectStatus(StrEnum):
    Draft = "Draft"
    Active = "Active"
    OnHold = "On_hold"
    Completed = "Completed"
    Archived = "Archived"
