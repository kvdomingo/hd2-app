from pydantic import BaseModel


class WarbondItem(BaseModel):
    item_id: int
    medal_cost: int


class Warbond(BaseModel):
    medals_to_unlock: int
    items: list[WarbondItem]
