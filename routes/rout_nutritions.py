from flask import jsonify

from app import session, app
from models.nutritions import Nutritions
from serializators.nutrition_serializer import NutritionsAliasList, NutritionsAlias


@app.route('/nutrition')
def food_id():
    nutrs = Nutritions.query.all()
    response = jsonify(NutritionsAliasList(alias=nutrs).dict())
    return response

@app.route('/nutrition/<int:nutrition_id>', methods=['GET'])
def nutr_id(nutrition_id):
    nutrs = session.query(Nutritions).filter_by(id=nutrition_id).first()
    data = NutritionsAlias.from_orm(nutrs)
    return jsonify(data.dict())