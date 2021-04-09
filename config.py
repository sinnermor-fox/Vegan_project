import os
from os import environ, path

basedir = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(path.join(basedir, '.env'))



class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    DB_NAME = 'postgres'
    ORIGINS = ['http://localhost:5000','http://127.0.0.1:5000']
    VAL = 'DEFAULT'
    DB_HOST = 'localhost'
    CORS_HEADERS = 'Content-Type'
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def DATABASE_URI(self):  # Note: all caps
        return 'postgresql://postgres:123456@{}:5432/{}'.format( self.DB_HOST, self.DB_NAME)



class ProductionConfig(Config):
    DEBUG = False
    VAL = 'PROD'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    VAL = 'STAGE'


class DevelopmentConfig(Config):
    # DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True