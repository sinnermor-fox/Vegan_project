from flask import jsonify, request

from app import app
from controls.algorithms.create_vegan import count_menu
from controls.menu_creator import get_menu_dressed
from serializators.food_serializer import FoodNettoListAlias, FoodNettoMenuAlias
from serializators.menu import MenuListAlias



@app.route('/menu/1', methods=['GET'])
def get_menu_daily():
    menu_data = count_menu()

    # Ниже алгоритм преобразования не кажется мне верным
    # How to create dressed entities
    dressed_list = []
    for item in menu_data:
        dressed_data = FoodNettoMenuAlias(food=item.description, netto=100)
        dressed_list.append(dressed_data)
    data = MenuListAlias(menu=dressed_list)
    return jsonify(data.dict())

# TODO fix cycle import
@app.route('/menu/<username>', methods=['GET'])
def get_menu_personaly(username):
    menu = get_menu_dressed(username)
    dressed_list = []
    for item in menu:
        dressed_data = FoodNettoMenuAlias(food=item.description, netto=item.MenuWeek.netto)
        dressed_list.append(dressed_data)
    data = MenuListAlias(menu=dressed_list)

    return jsonify(data.dict())

