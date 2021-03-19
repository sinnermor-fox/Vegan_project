from flask import jsonify, request

from app import app, session, db
from controls.algorithms.create_vegan import count_menu
from models.food import Food
from models.menu_week import MenuWeek
from models.users import User
from serializators.food_serializer import FoodNettoListAlias, FoodNettoMenuAlias
from serializators.menu import MenuListAlias
from serializators.nutrition_serializer import NutritionsAlias


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

@app.route('/menu/<username>', methods=['GET'])
def get_menu_personaly(username):

    user_data = session.query(User).filter(User.telegram_account==username).first()
    menu = session.query(MenuWeek, Food.description).filter(MenuWeek.user_id==user_data.id).all()

    dressed_list = []
    for item in menu:
        dressed_data = FoodNettoMenuAlias(food=item.description, netto=item.MenuWeek.netto)
        dressed_list.append(dressed_data)
    data = MenuListAlias(menu=dressed_list)

    return jsonify(data.dict())

