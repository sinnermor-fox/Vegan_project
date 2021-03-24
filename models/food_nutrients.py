from app import db


class FoodNutrients(db.Model):
    """
        Class of binding food and nutritions in it.
        There are some nutritions with different values for every food item
    """

    __tablename__ = 'food_nutrients'
    id = db.Column(db.Integer, primary_key=True)
    nutrition_value = db.Column(db.Float, nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey('food.id'), nullable=False)
    nutrition_id = db.Column(db.Integer, db.ForeignKey('nutritions.id'), nullable=False)

    def __repr__(self):
        return f'<Food {self.food_id} - Nutrition {self.nutrition}>'