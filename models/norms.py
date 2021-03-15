from app import db


class Norms(db.Model):
    __tablename__ = 'norms'
    id = db.Column(db.Integer, primary_key=True)
    sex = db.Column(db.Boolean, nullable=False)
    min_age = db.Column(db.Integer, nullable=False)
    max_age = db.Column(db.Integer, nullable=False)
    nutrition_id = db.Column(db.Integer, db.ForeignKey('nutritions.id'), nullable=False)
    norm_value = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(80), nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    # nutrition = db.relationship('Nutrition', backref=db.backref('nutrition', lazy=True))

    def __repr__(self):
        return '<Norms %r %r-%r %r %r>' % self.sex % self.min_age %self.max_age %self.nutrition_id %self.norm_value
