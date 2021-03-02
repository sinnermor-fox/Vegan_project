# Эта функция позволит нам обновить книги и сохранить их в базе данных.
import json
import logging

from flask import jsonify

from app import app, session
from models.food import Food
from models.nutritions import Nutritions


@app.route('/1')
def food_id():
    food = session.query(Nutritions).all()
    response = json.dumps(food)
    response.status_code = 200
    return response



@app.route('/food')
def food():
    food = session.query(Nutritions).all()
    logging.info(food)
    # response = json.dump(food)
    # response.status_code = 200
    # response.headers['Location'] = url_for('api_v1.get_user', id=customer.user.id)
    return str(food)
