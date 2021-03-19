import datetime

from app import db


#TODO придумать как идентифицировать меню по дням недели
#TODO переименовать таблицу
class MenuWeek(db.Model):
    """
        Class for storing counted menus for users
    """

    __tablename__ = 'menu_week'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    food_id = db.Column(db.Integer, nullable=False)
    netto = db.Column(db.Integer, nullable=False)
    creation_date = db.Column(db.Date, nullable=False)

    def __init__(self, user_id, food_id, netto):
        self.user_id = user_id
        self.food_id = food_id
        self.netto = netto
        self.creation_date = datetime.date.today()

