from flask_sqlalchemy import Model
from sqlalchemy import Column, Integer, String, Boolean, Date


class User(Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(180), nullable=False)
    lastname = Column(String(180), nullable=False)
    sex = Column(Boolean)
    birthday = Column(Date)
    email = Column(String)
    telegram_account = Column(String)