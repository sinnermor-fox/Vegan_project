from flask import jsonify
from flask_cors import cross_origin

from app import  app
from src.models.nutritions import Nutritions
from src.serializators.nutrition_serializer import NutritionsAliasList, NutritionsAlias


@app.route('/api/nutrition')
@cross_origin(allow_headers=['Content-Type'])
def nutrition_all():
    nutrition = Nutritions.query.all()
    response = jsonify(NutritionsAliasList(nutritions=nutrition).dict())
    return response


@app.route('/api/nutrition/<int:nutrition_id>', methods=['GET'])
@cross_origin(allow_headers=['Content-Type'])
def nutrition_by_id(nutrition_id):
    nutrition = Nutritions.query.filter_by(id=nutrition_id).first()
    data = NutritionsAlias.from_orm(nutrition)
    return jsonify(data.dict())