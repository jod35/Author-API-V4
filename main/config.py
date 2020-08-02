import os

db_user=os.environ.get('MYSQL_USER') or 'jona'
db_password=os.environ.get('MYSQL_PASSWORD') or 'nathanoj35'

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'c495ddff1e5a1284a317cf053d3b8cf0245c01090c4b0e6c279373ffad1ed631'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://{}:{}@localhost/author_db'.format(db_user,db_password)
    DEBUG=True
