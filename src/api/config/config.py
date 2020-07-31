class Config(object):
    DEBUG=False
    TESTING=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=''

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI=''
    DEBUG=False
    SQLALCHEMY_ECHO=False

class TestingConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI=''
    SQLALCHEMY_ECHO=False


