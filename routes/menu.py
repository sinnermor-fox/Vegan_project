import flask
from flask import jsonify, request

from app import app
from controls.menu_creator import get_menu_dressed
from serializators.food_serializer import FoodNettoListAlias, FoodNettoMenuAlias
from serializators.menu import MenuListAlias


@app.route('/menu/<username>', methods=['GET'])
def menu_personally(username: str) -> flask.Response:
    menu = get_menu_dressed(username)
    list_comprehension = [FoodNettoMenuAlias(food=item.description, netto=item.MenuWeek.netto) for item in menu]
    data = MenuListAlias(menu=list_comprehension)
    return jsonify(data.dict())

