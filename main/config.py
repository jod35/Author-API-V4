import os
from decouple import config

# db_user=config('DB_USER')
# db_password=config('DB_PASSWORD')

BASE_DIR=os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'c495ddff1e5a1284a317cf053d3b8cf0245c01090c4b0e6c279373ffad1ed631'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(BASE_DIR,'app.db')
    DEBUG=True
