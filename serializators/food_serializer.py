from typing import List

from pydantic import BaseModel


class FoodModel(BaseModel):
    id: int
    description: str

    class Config:
        orm_mode = True


class FoodNettoAlias(BaseModel):
    id: int
    description: str
    food_group_id: int
    # netto: int

    class Config:
        orm_mode = True


class FoodNettoListAlias(BaseModel):
    food : List[FoodNettoAlias]

    class Config:
        orm_mode = True
