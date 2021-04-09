from app import db


class Food(db.Model):
    """
        Class for food.
        Each food has id, description and it's food_group
    """
    __tablename__ = 'food'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(180), nullable=False)
    food_group_id = db.Column(db.Integer, db.ForeignKey('food_group.id'), nullable=False)

    def __repr__(self):
        return '<Food %r>' % self.description
