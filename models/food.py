import json

from flask import jsonify
from flask_pydantic import validate
from flask_sqlalchemy import Model
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

# from app import  app


class Food(Model):
    __tablename__ = 'food'
    id = Column(Integer, primary_key=True)
    description = Column(String(180), nullable=False)
    food_group_id = Column(Integer, ForeignKey('food_group.id'), nullable=False)
    food_group = relationship('FoodGroup', backref=backref('food_group', lazy=True))

    def __repr__(self):
        return '<Food %r>' % self.description


class FoodModel(BaseModel):
    id: int
    description: str

    class Config:
        orm_mode = True


# # Example2: request body only
# @app.route("/food/<id>", methods=["GET"])
# def get(id):
#     food = Food.query.filter_by(id=id)
#     response = jsonify(food.to_dict())
#     response.status_code = 200
#     # response.headers['Location'] = url_for('api_v1.get_user', id=customer.user.id)
#     return response