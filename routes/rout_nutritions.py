from flask import jsonify

from app import  app
from models.nutritions import Nutritions
from serializators.nutrition_serializer import NutritionsAliasList, NutritionsAlias


@app.route('/nutrition')
def food_id():
    nutrition = Nutritions.query.all()
    response = jsonify(NutritionsAliasList(alias=nutrition).dict())
    return response


@app.route('/nutrition/<int:nutrition_id>', methods=['GET'])
def nutrition_by_id(nutrition_id):
    nutrition = Nutritions.query.filter_by(id=nutrition_id).first()
    data = NutritionsAlias.from_orm(nutrition)
    return jsonify(data.dict())