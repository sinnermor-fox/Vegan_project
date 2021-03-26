from celery import Celery
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
celery.autodiscover_tasks()

db = SQLAlchemy(app)

@celery.task()
def hello():
    print("Hello there")

task = hello.delay()

import routes.route_food
import routes.rout_nutritions
import routes.menu

