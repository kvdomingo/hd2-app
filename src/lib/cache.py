from pydantic import BaseModel
from redis import asyncio as aioredis

from src.settings import settings

redis = aioredis.from_url(settings.REDIS_URL)


async def cache_set[T](key: str, value: T) -> None:
    if isinstance(value, BaseModel):
        v = value.model_dump(mode="json")
    else:
        v = value

    await redis.set(key, v)


async def cache_get[T](key: str) -> T | None:
    return await redis.get(key)
