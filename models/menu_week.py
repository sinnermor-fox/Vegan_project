from flask_sqlalchemy import Model
from sqlalchemy import Column, Integer, String, Date


class MenuWeek(Model):
    """
        Class for storing counted menus for users
    """

    __tablename__ = 'menu_week'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    food_id = Column(Integer, nullable=False)
    netto = Column(Integer, nullable=False)
    creation_date = Column(Date, nullable=False)
