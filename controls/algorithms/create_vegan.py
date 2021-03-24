import csv
import itertools
import logging
import random
from pathlib import Path

from sqlalchemy import func, funcfilter
from operator import itemgetter
from app import db
from config import basedir
from models.food import Food
from models.food_nutrients import FoodNutrients
from models.norms import Norms
from models.nutritions import Nutritions

"""
Тут у нас логика подбора продуктов . Я думаю что тут будет 2 блока
- продукты на день
- продукты на неделю (допустим 7 раз продукты на день)
Версия 1 - на основе файла data/basic_menu.csv
1. Берем определенное кол-во товаров из кажддой группы (тут потом будет логика кол-ва грамм по группам)
2. Расчитываем получившиеся знаения нутриентов
3. Сравниванием с таблицей норм в значении и процентах (сейчас есть проблема с тем,
 что есть отрацательные значения и проблема с данными)
 question - Тут по идее надо работать с сортировками внутри списка объектов, я придумала только через  list comprehension
4.  Сейчас это результат list(Food), наверно олжен быть 
MenuListAlias(должен ли он из контрола приходить в форме json и где обогощать данные)
"""

units = {'mg': 1, 'µg': 0.001, 'g': 1000}


def get_food_nutritions(foods):
    food_ids = [el.id for el in foods]
    print(food_ids)
    counted_nutrs_filtered = db.session.query(
        FoodNutrients.nutrition_id,
        func.sum(FoodNutrients.nutrition_value),
    ).filter(
        FoodNutrients.food_id.in_(food_ids)
    ).filter(
        FoodNutrients.nutrition_id == Nutritions.id
    ).group_by(
        FoodNutrients.nutrition_id
    ).all()
    return counted_nutrs_filtered


def get_random_food(group_id, count):
    food_data = Food.query.filter(
                    Food.food_group_id == group_id
                ).order_by(
                    func.random()
                ).limit(count).all()
    return food_data


# TODO добавить поддержку нетто, тут по идее на выходе должны уже создаваться новые обекты
def based_csv_menu():
    menu_structure, food_result = [], []
    with open(Path(basedir, 'data', 'basic_menu.csv'), 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            menu_structure.append(row)
    for part in menu_structure:
        food = get_random_food(part['group_id'], part['count'])
        food_result.append(food)
    return list(itertools.chain(*food_result))


def get_norms(sex: bool = True, age: int = 30):
    norms = db.session.\
        query(
            Norms.nutrition_id,
            Norms.norm_value
        ).filter(
            Norms.sex == sex,
            Norms.min_age <= age,
            Norms.max_age >= age
    ).all()
    return norms


def count_units(nutrition_id):
    norm_unit = db.session.query(
            Norms.nutrition_id, Norms.unit, Nutritions.unit
        ).filter(
            Norms.nutrition_id == nutrition_id,
            Norms.nutrition_id == Nutritions.id

        ).first()
    if norm_unit[1] != f"{norm_unit.unit}/d":
        norm = units[norm_unit[1][:-2]]
        menu = units[norm_unit[2]]
    else:
        norm = 1
        menu = 1
    return {'norm': norm, 'menu': menu}


def get_difference(menu_nutrition, norm_nutrition):
    difference, errors = [], []
    menu_dict = dict(menu_nutrition)
    for nutrition in norm_nutrition:
        units = count_units(nutrition.nutrition_id)
        if menu_dict.get(nutrition.nutrition_id):
            diff = float((nutrition.norm_value * units['norm']) -
                         (menu_dict[nutrition.nutrition_id] * units['menu']))
            dif_percent = (diff / nutrition.norm_value * units['norm']) * 100
            difference.append({'nutrition_id': nutrition.nutrition_id,
                               'percent': dif_percent, 'diff': diff,
                               'norm': (nutrition.norm_value * units['norm']),
                               'menu': (menu_dict[nutrition.nutrition_id] * units['menu'])})

        else:
            print(f"У нас нет значения {nutrition.nutrition_id} в меню")
            errors.append(f'У нас нет значения {nutrition.nutrition_id} в меню')
    with open('error.txt', 'w') as f:
        for line in errors:
            f.writelines(line)
    d2 = sorted(difference, key=itemgetter('percent'))
    return d2


def analise_menu(diff_massive):
    sorted_menu = sorted(diff_massive, key=itemgetter('percent'))
    return sorted_menu


def count_menu(name='based_csv'):
    food_list_1 = based_csv_menu()
    return food_list_1

#
# food_list_1 = based_csv_menu()
# counted_nutrs_filtered = get_food_nutritions(food_list_1)
# norms = get_norms()
# diff = get_difference(counted_nutrs_filtered, norms)
# with open('diff.txt', 'w') as f:
#     for line in diff:
#         f.writelines(f"{str(line)}\n")