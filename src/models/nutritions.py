import typing

from flask import jsonify
from pydantic import BaseModel

from app import db, app


class Nutritions(db.Model):
    """
        Class for model Nutrition with data about name, tag and unit
    """

    __tablename__ = 'nutritions'
    id = db.Column(db.Integer, primary_key=True)
    unit = db.Column(db.String(80), nullable=False)
    tag = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Nutrition %r>' % self.name



