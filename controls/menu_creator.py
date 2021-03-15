import csv
import itertools
import logging
import random
from sqlalchemy import func, funcfilter

from app import session
from config import basedir
from models.food import Food
from models.food_nutrients import FoodNutrients
from models.norms import Norms

def get_food_nutritions(foods):
    food_ids = [el.id for el in foods]
    counted_nutrs_filtered = session.query(FoodNutrients.nutrition_id, func.sum(FoodNutrients.nutrition_value)). \
        filter(FoodNutrients.food_id.in_(food_ids)). \
        group_by(FoodNutrients.nutrition_id).all()
    return counted_nutrs_filtered


def get_random_food(group_id, count):
    food_data = Food.query.filter(Food.food_group_id == group_id).order_by(func.random()).limit(count).all()
    return food_data

def based_csv_menu():
    menu_structure, food_result = [], []
    with open(f'{basedir}/data/basic_menu.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            menu_structure.append(row)
    for part in menu_structure:
        food = get_random_food(part['group_id'], part['count'])
        food_result.append(food)
    return list(itertools.chain(*food_result))

def get_norms(sex: bool = True, age: int = 30):
    norms = session.query(Norms.nutrition_id, Norms.norm_value).filter(Norms.sex == sex, Norms.min_age <= age, Norms.max_age >= age).all()
    return norms

def get_difference(menu_nutitions, norm_nutritions):
    difference = []
    for nutrition in norm_nutritions:
        if menu_nutitions[nutrition.nutrition_id]:
            difference.append({nutrition.nutrition_id: float(nutrition.norm_value-menu_nutitions[nutrition.nutrition_id])})
    return difference

food_list_1 = based_csv_menu()
counted_nutrs_filtered = get_food_nutritions(food_list_1)
norms = get_norms()
diff  = get_difference(counted_nutrs_filtered, norms)
print(diff)