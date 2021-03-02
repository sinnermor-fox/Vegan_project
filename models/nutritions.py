from flask import jsonify

from app import db, app


class Nutritions(db.Model):
    __tablename__ = 'nutritions'
    id = db.Column(db.Integer, primary_key=True)
    unit = db.Column(db.String(80), nullable=False)
    tag = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Nutrition %r>' % self.name

@app.route("/nutr", methods=["GET"])
def get():
    nutr = Nutritions.query.all()
    response = jsonify(nutr.to_dict())
    response.status_code = 200
    # response.headers['Location'] = url_for('api_v1.get_user', id=customer.user.id)
    return response


