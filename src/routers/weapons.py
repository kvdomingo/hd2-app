import orjson
from aiofiles import open
from fastapi import APIRouter, Request

from src.lib.rate_limit import limiter
from src.schemas.weapons import Grenade, PrimaryWeapon, SecondaryWeapon
from src.settings import settings

router = APIRouter(prefix="/weapons", tags=["weapons"])


@router.get("/primaries", response_model=dict[int, PrimaryWeapon])
@limiter.limit(settings.GLOBAL_DEFAULT_RATE_LIMIT)
async def list_primaries(request: Request):
    async with open(settings.BASE_DIR / "hd2-json/items/weapons/primary.json") as f:
        return orjson.loads(await f.read())


@router.get("/secondaries", response_model=dict[int, SecondaryWeapon])
@limiter.limit(settings.GLOBAL_DEFAULT_RATE_LIMIT)
async def list_secondaries(request: Request):
    async with open(settings.BASE_DIR / "hd2-json/items/weapons/secondary.json") as f:
        return orjson.loads(await f.read())


@router.get("/grenades", response_model=dict[int, Grenade])
@limiter.limit(settings.GLOBAL_DEFAULT_RATE_LIMIT)
async def list_grenades(request: Request):
    async with open(settings.BASE_DIR / "hd2-json/items/weapons/grenades.json") as f:
        return orjson.loads(await f.read())


@router.get("/fire-modes", response_model=dict[int, str])
@limiter.limit(settings.GLOBAL_DEFAULT_RATE_LIMIT)
async def list_fire_modes(request: Request):
    async with open(settings.BASE_DIR / "hd2-json/items/weapons/fire_modes.json") as f:
        return orjson.loads(await f.read())


@router.get("/traits", response_model=dict[int, str])
@limiter.limit(settings.GLOBAL_DEFAULT_RATE_LIMIT)
async def list_traits(request: Request):
    async with open(settings.BASE_DIR / "hd2-json/items/weapons/traits.json") as f:
        return orjson.loads(await f.read())


@router.get("/types", response_model=dict[int, str])
@limiter.limit(settings.GLOBAL_DEFAULT_RATE_LIMIT)
async def list_types(request: Request):
    async with open(settings.BASE_DIR / "hd2-json/items/weapons/types.json") as f:
        return orjson.loads(await f.read())
