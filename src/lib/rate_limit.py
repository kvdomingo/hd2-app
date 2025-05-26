from fastapi import HTTPException, Request, status
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from src.settings import settings

limiter = Limiter(key_func=get_remote_address, storage_uri=settings.REDIS_URL)


def rate_limit_exceeded_handler(_: Request, __: RateLimitExceeded):
    raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS)
