import logging
import random

from sqlalchemy import func

from models.food import Food

# def q(filter, page=0, page_size=None):
#     query = session.query(...).filter(filter)
#     if page_size:
#         query = query.limit(page_size)
#     if page:
#         query = query.offset(page*page_size)
#     return query
#
from models.food_nutrients import FoodNutrients


def get_food_nutritions(food_id: int):
    food_nutrients = FoodNutrients.query.filter(FoodNutrients.food_id == food_id).first()
    return food_nutrients

def get_food_to_menu(group_id, count):
    food_data = Food.query.filter(Food.food_group_id == group_id).order_by(func.random()).limit(count).all()
    food_nutrients = FoodNutrients.query.filter(FoodNutrients.food_id == food_data[0]).first()
    # for data in food_data:

    return food_data


def get_food_menu_v2(group_id, count):
    i = 0
    result = []
    while i < count:
        food_data = Food.query.filter(Food.food_group_id == group_id).all()
        random_value = random.randrange(0, len(food_data))
        logging.info(food_data[random_value])
        if food_data[random_value] not in result:
            result.append(food_data[random_value])
            i += 1
    return result
