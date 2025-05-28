import orjson
from aiofiles import open
from fastapi import APIRouter, Request

from src.lib.rate_limit import limiter
from src.schemas.warbonds import Warbond
from src.settings import settings

router = APIRouter(prefix="/warbonds", tags=["warbonds"])


@router.get("", response_model=dict[str, dict[int, Warbond]])
@limiter.limit(settings.GLOBAL_DEFAULT_RATE_LIMIT)
async def list_warbonds(request: Request):
    out = {}
    for path in (settings.BASE_DIR / "hd2-json/warbonds").glob("*.json"):
        async with open(path) as f:
            data = orjson.loads(await f.read())

        out[path.stem] = data

    return out
