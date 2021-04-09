from typing import List

from pydantic import BaseModel

from src.serializators.food_serializer import FoodNettoMenuAlias


class MenuListAlias(BaseModel):
    menu: List[FoodNettoMenuAlias]

    class Config:
        orm_mode = True


class MenuWeekAlias(BaseModel):
    day: str
    menu: List[FoodNettoMenuAlias]

    class Config:
        orm_mode = True