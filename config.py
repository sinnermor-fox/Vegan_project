import os
from os import environ, path

basedir = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(path.join(basedir, '.env'))



class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    DB_NAME = 'postgres'
    VAL = 'DEFAULT'
    DB_HOST = 'localhost'
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def DATABASE_URI(self):  # Note: all caps
        return 'postgresql://postgres:123456@{}:5432/postgres'.format( self.DB_HOST)



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