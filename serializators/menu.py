from typing import List

from pydantic import BaseModel

from serializators.food_serializer import FoodNettoMenuAlias


class MenuListAlias(BaseModel):
    menu : List[FoodNettoMenuAlias]

    class Config:
        orm_mode = True