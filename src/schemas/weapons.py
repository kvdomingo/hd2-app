from pydantic import BaseModel

from .base import GenericNameDescription


class Weapon(BaseModel):
    name: str
    description: str
    damage: int
    capacity: int
    recoil: int
    fire_rate: int
    fire_mode: list[int]
    traits: list[int]


class PrimaryWeapon(Weapon):
    type: int


class SecondaryWeapon(Weapon):
    pass


class Grenade(GenericNameDescription):
    damage: int
    penetration: int
    outer_radius: int
    fuse_time: float
