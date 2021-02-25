from app import db


class FoodGroup(db.Model):
    __tablename__ = 'food_group'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(180),  nullable=False)

    def __repr__(self):
        return '<FoodGroup %r>' % self.description


class Nutritions(db.Model):
    __tablename__ = 'nutritions'
    id = db.Column(db.Integer, primary_key=True)
    unit = db.Column(db.String(80), nullable=False)
    tag = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Nutrition %r>' % self.name


class Food(db.Model):
    __tablename__ = 'food'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(180), nullable=False)
    food_group_id = db.Column(db.Integer, db.ForeignKey('food_group.id'), nullable=False)
    food_group = db.relationship('FoodGroup', backref=db.backref('food_group', lazy=True))

    def __repr__(self):
        return '<Food %r>' % self.description


class FoodNutrients(db.Model):
    __tablename__ = 'food_nutrients'
    id = db.Column(db.Integer, primary_key=True)
    nutrition_value = db.Column(db.Float, nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey('food.id'), nullable=False)
    nutrition_id = db.Column(db.Integer, db.ForeignKey('nutritions.id'), nullable=False)
    food = db.relationship('Food', backref=db.backref('food', lazy=True))
    nutrition = db.relationship('Nutrition', backref=db.backref('nutrition', lazy=True))

    def __repr__(self):
        return f'<Food {self.food_id} - Nutrition {self.nutrition}>'