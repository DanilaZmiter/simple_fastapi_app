from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent


class DatabaseSettings(BaseModel):
    url: str
    echo: bool


class Settings(BaseSettings):
    db: DatabaseSettings

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",  # path
        env_nested_delimiter="__",  # delimeter for taking .env variables in correct way
        env_file_encoding="utf-8",  # encoding of .env file
        extra="ignore",  # ignore another variables that could be in .env in future but wont be in Settings
    )


settings = Settings()  # type: ignore because of pylance is scream at me for missing some parameters but pydantic settings take it by itself
