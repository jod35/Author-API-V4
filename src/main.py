import os
from flask import Flask
from api.utils.database import db




if os.environ.get('WORK_ENV') =='PROD':
    app_config=ProdConfig

elif os.environ.get('WOKR_ENV') == 'TEST':
    app_config=TestConfig

else:
    app_config=DevConfig






def create_app(config):
    app=Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)

    with app.app_context():
        db.create_all()
    
    return app


if __name__ == "__main__":
    app.run(port=5000,host="0.0.0.0",use_reloader=False)

