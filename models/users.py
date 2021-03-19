from flask_sqlalchemy import Model
from sqlalchemy import Column, Integer, String, Boolean, Date

from app import db


class User(db.Model):

    """
        Class for store user information
    """

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(180), nullable=False)
    lastname = db.Column(db.String(180), nullable=False)
    sex = db.Column(db.Boolean)
    birthday = db.Column(db.Date)
    email = db.Column(db.String)
    telegram_account = db.Column(db.String)