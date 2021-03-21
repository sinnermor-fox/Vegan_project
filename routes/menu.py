import flask
from flask import jsonify, request

from app import app
from controls.algorithms.create_vegan import count_menu
from controls.menu_creator import get_menu_dressed
from serializators.food_serializer import FoodNettoListAlias, FoodNettoMenuAlias
from serializators.menu import MenuListAlias


@app.route('/menu/1', methods=['GET'])
def get_menu_daily():
    menu_data = count_menu()
    dressed_list = []
    for item in menu_data:
        dressed_data = FoodNettoMenuAlias(food=item.description, netto=100)
        dressed_list.append(dressed_data)
    data = MenuListAlias(menu=dressed_list)
    return jsonify(data.dict())


@app.route('/menu/<username>', methods=['GET'])
def menu_personally(username: str) -> flask.Response:
    menu = get_menu_dressed(username)
    dressed_list = []
    for item in menu:
        dressed_data = FoodNettoMenuAlias(food=item.description, netto=item.MenuWeek.netto)
        dressed_list.append(dressed_data)
    data = MenuListAlias(menu=dressed_list)

    return jsonify(data.dict())

