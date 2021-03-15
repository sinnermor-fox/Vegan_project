from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123456@localhost:5432/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Base = declarative_base()

engine = create_engine('postgresql://postgres:123456@localhost:5432/postgres')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


import routes.route_food
import routes.rout_nutritions

