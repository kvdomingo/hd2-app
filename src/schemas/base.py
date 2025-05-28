from pydantic import BaseModel


class GenericNameDescription(BaseModel):
    name: str
    description: str
