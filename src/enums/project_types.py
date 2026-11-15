from enum import StrEnum


class ProjectTypesBusiness(StrEnum):
    Production = "PRODUCTION"
    Internal = "INTERNAL"
    Custom = "CUSTOM"


class ProjectTypesDirection(StrEnum):
    SoftwareDevelopment = "SOFTWARE DEVELOPMENT"
    InfrastructureAndDevOPS = "INFRASTRUCTURE AND DEVOPS"
    DataAIML = "DATA/AI/ML"
    Integration = "INTEGRATION"
    InfoSec = "INFOSEC"


class ProjectTypesLifeCycle(StrEnum):
    Greenfield = "GREENFIELD"
    Brownfield = "BROWNFIELD"
    MigrationRefactoring = "MIGRATION/REFACTORING"
    Support = "SUPPORT"


class ProjectTypesDifficulty(StrEnum):
    Predictable = "PREDICTABLE"
    Complex = "COMPLEX"
    RandD = "R&D"
