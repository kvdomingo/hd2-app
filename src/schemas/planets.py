from pydantic import BaseModel


class Planet(BaseModel):
    name: str
    sector: str
    biome: str
    environmentals: list[str]
    names: dict[str, str]
    type: str
    weather_effects: list[str]


class GenericNameDescription(BaseModel):
    name: str
    description: str


class PlanetRegion(GenericNameDescription):
    pass


class Biome(GenericNameDescription):
    pass


class Environmental(GenericNameDescription):
    pass
