from app import db


class Food(db.Model):
    __tablename__ = 'food'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(180), nullable=False)
    food_group_id = db.Column(db.Integer, db.ForeignKey('food_group.id'), nullable=False)
    # food_group = db.relationship('FoodGroup', backref=db.backref('food_group', lazy=True))

    def __repr__(self):
        return '<Food %r>' % self.description



# # Example2: request body only
# @app.route("/food/<id>", methods=["GET"])
# def get(id):
#     food = Food.query.filter_by(id=id)
#     response = jsonify(food.to_dict())
#     response.status_code = 200
#     # response.headers['Location'] = url_for('api_v1.get_user', id=customer.user.id)
#     return response