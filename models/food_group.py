from app import db


class FoodGroup(db.Model):
    __tablename__ = 'food_group'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(180),  nullable=False)

    def __repr__(self):
        return '<FoodGroup %r>' % self.description