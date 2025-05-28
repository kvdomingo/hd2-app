import orjson
from aiofiles import open
from fastapi import APIRouter, Request

from src.lib.rate_limit import limiter
from src.schemas.planets import Biome, Environmental, Planet, PlanetRegion
from src.settings import settings

router = APIRouter(prefix="/planets", tags=["planets"])


@router.get("", response_model=dict[int, Planet])
@limiter.limit(settings.GLOBAL_DEFAULT_RATE_LIMIT)
async def list_planets(request: Request):
    async with open(settings.BASE_DIR / "hd2-json/planets/planets.json") as f:
        return orjson.loads(await f.read())


@router.get("/regions", response_model=dict[int, PlanetRegion])
@limiter.limit(settings.GLOBAL_DEFAULT_RATE_LIMIT)
async def list_planet_regions(request: Request):
    async with open(settings.BASE_DIR / "hd2-json/planets/planetRegion.json") as f:
        return orjson.loads(await f.read())


@router.get("/biomes", response_model=dict[str, Biome])
@limiter.limit(settings.GLOBAL_DEFAULT_RATE_LIMIT)
async def list_biomes(request: Request):
    async with open(settings.BASE_DIR / "hd2-json/planets/biomes.json") as f:
        return orjson.loads(await f.read())


@router.get("/environmentals", response_model=dict[str, Environmental])
@limiter.limit(settings.GLOBAL_DEFAULT_RATE_LIMIT)
async def list_environmentals(request: Request):
    async with open(settings.BASE_DIR / "hd2-json/planets/environmentals.json") as f:
        return orjson.loads(await f.read())
