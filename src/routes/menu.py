import flask
from flask import jsonify, request, make_response, Response
from flask_cors import cross_origin

from app import app
from src.controls.menu_creator import get_menu_dressed, create_day_menu_manual, create_menu_week
from src.serializators.food_serializer import FoodNettoMenuAlias
from src.serializators.menu import MenuListAlias


@app.route('/api/menu/<user_account>', methods=['GET', 'POST'])
def menu_personally(user_account: str) -> flask.Response:
    if request.method == 'POST':
        response = create_day_menu_manual(user_account, 1)
        resp = Response({'status': response['status']}, status=response['status_code'],
                        mimetype='application/json')
        return resp
    else:
        menu = get_menu_dressed(user_account, day='today')
        list_food_menu = [FoodNettoMenuAlias(food=item.description,
                                             netto=item.MenuWeek.netto,
                                             day=1)
                          for item in menu]
        data = MenuListAlias(menu=list_food_menu)
        return jsonify(data.dict())


@app.route('/api/internal/menu/week/<user_account>', methods=['POST'])
def internal_week_menu(user_account: str):
    """API endpoint to count menu for a week. Is internal and called from celery"""
    response = create_menu_week(user_account)
    if response:
        resp = make_response({'errors': response})
    else: resp = make_response({'status': 'ok'})
    resp.headers['Content-Type'] = "application/json"
    return resp


# Не очень понимаю как быть с форматом вывода
@app.route('/api/menu/week/<user_account>', methods=['get'])
def week_menu(user_account: str):
    menu = get_menu_dressed(user_account, day='week')
    list_food_menu = [FoodNettoMenuAlias(food=item.description,
                                         netto=item.MenuWeek.netto,
                                         day=item.MenuWeek.day_id)
                      for item in menu]
    data = MenuListAlias(menu=list_food_menu)
    return jsonify(data.dict())
