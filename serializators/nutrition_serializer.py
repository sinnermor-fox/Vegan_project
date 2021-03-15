import typing

from pydantic import BaseModel


class NutritionsAlias(BaseModel):
    unit: str
    tag: str
    name: str

    class Config:
        orm_mode = True


class NutritionsAliasList(BaseModel):
    nutritions: typing.List[NutritionsAlias]

    class Config:
        orm_mode = True
