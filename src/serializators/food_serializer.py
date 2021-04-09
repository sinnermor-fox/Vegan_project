from typing import List

from pydantic import BaseModel


class FoodModel(BaseModel):
    id: int
    description: str

    class Config:
        orm_mode = True


#TODO разобраться как игнорировать поля
# при создании и валидации результирующего объекта
class FoodNettoAlias(BaseModel):
    id: int
    description: str
    food_group_id: int
    # netto: int

    class Config:
        orm_mode = True


class FoodNettoListAlias(BaseModel):
    food: List[FoodNettoAlias]

    class Config:
        orm_mode = True


class FoodNettoMenuAlias(BaseModel):
    food: str
    netto: int
    day: int

    class Config:
        orm_mode = True

