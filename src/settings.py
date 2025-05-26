from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    REDIS_URL: str = "redis://localhost:6379"


@lru_cache
def _get_settings() -> Settings:
    return Settings()


settings = _get_settings()
