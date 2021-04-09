from flasgger import Swagger
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
swagger = Swagger(app)
db = SQLAlchemy(app)
CORS(app,  resources={ r'/*': {'origins': app.config['ORIGINS']}})



from src.routes import menu
from src.routes import rout_nutritions
from src.routes import route_food




