from configuration.environment import env
from flask_sqlalchemy import SQLAlchemy

DATABASE_URL = env.str('SQLALCHEMY_DATABASE_URI')

# Config file utilized to migrate db with SQLAlchemy
class SQLAlchemyConfig:
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()