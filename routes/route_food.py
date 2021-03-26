from flask import jsonify

from app import app
from models.food import Food

from serializators.food_serializer import FoodNettoListAlias


@app.route('/food')
def food():
    food_data = Food.query.all()
    responce = FoodNettoListAlias.from_orm(food_data)
    return jsonify(responce)
