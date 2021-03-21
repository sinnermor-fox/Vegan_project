from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)
# Base = declarative_base()

# engine = create_engine(app.config.get('SQLALCHEMY_DATABASE_URI'))
# Base.metadata.bind = engine
# DBSession = sessionmaker(bind=engine)
# session = DBSession()


import routes.route_food
import routes.rout_nutritions
import routes.menu

