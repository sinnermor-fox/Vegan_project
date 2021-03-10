from app import db


class FoodNutrients(db.Model):
    __tablename__ = 'food_nutrients'
    id = db.Column(db.Integer, primary_key=True)
    nutrition_value = db.Column(db.Float, nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey('food.id'), nullable=False)
    nutrition_id = db.Column(db.Integer, db.ForeignKey('nutritions.id'), nullable=False)
    # food = db.relationship('Food', backref=db.backref('food', lazy=True))
    # nutrition = db.relationship('Nutrition', backref=db.backref('nutrition', lazy=True))

    def __repr__(self):
        return f'<Food {self.food_id} - Nutrition {self.nutrition}>'