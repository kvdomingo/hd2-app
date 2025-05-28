from pydantic import BaseModel

from .base import GenericNameDescription


class Planet(BaseModel):
    name: str
    sector: str
    biome: str
    environmentals: list[str]
    names: dict[str, str]
    type: str
    weather_effects: list[str]


class PlanetRegion(GenericNameDescription):
    pass


class Biome(GenericNameDescription):
    pass


class Environmental(GenericNameDescription):
    pass


class Effect(GenericNameDescription):
    galacticEffectId: int
