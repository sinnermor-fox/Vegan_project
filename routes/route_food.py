# Эта функция позволит нам обновить книги и сохранить их в базе данных.
import json
import logging
import random

from flask import jsonify

from app import app, session
from controls.menu_creator import get_food_to_menu
from models.food import Food
from models.food_group import FoodGroup
from serializators.food_serializer import FoodNettoListAlias


@app.route('/food')
def food():
    food_data = get_food_to_menu(1100, 3)
    responce = FoodNettoListAlias.from_orm(food_data)
    return jsonify(responce)
