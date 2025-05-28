from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import computed_field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PYTHON_ENV: Literal["local", "dev", "stg", "prod"] = "local"
    BASE_DIR: Path = Path(__file__).parent.parent
    REDIS_URL: str = "redis://redis:6379"
    GLOBAL_DEFAULT_RATE_LIMIT: str = "5/second"

    @computed_field
    @property
    def IS_LOCAL(self) -> bool:
        return self.PYTHON_ENV == "local"

    @computed_field
    @property
    def IS_PRODUCTION(self) -> bool:
        return self.PYTHON_ENV == "prod"


@lru_cache
def _get_settings() -> Settings:
    return Settings()


settings = _get_settings()
