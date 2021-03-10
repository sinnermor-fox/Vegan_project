from flask_sqlalchemy import Model
from sqlalchemy import Column, Integer, String, Date

# user_id
# date_create
# day
# food
# {"food_id_1": netto, "food_id_2": netto ...}
class MenuWeek(Model):
    __tablename__ = 'menu_week'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    food_id = Column(Integer, nullable=False)
    netto = Column(Integer, nullable=False)
    creation_date = Column(Date, nullable=False)
