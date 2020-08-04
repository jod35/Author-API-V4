from flask import Flask
from .config import DevConfig
from main.utils.database import db
from flask import jsonify,make_response
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager



app=Flask(__name__)

app.config.from_object(DevConfig)
db.init_app(app)

migrate=Migrate(app,db)

jwt=JWTManager(app)
from main.api.views import api_blueprint
from main.auth.views import auth_blueprint


app.register_blueprint(api_blueprint,url_prefix='/api')
app.register_blueprint(auth_blueprint,url_prefix='/auth')


@app.errorhandler(404)
def not_found(err):
    return make_response(
        jsonify({
            "message":"The endpoint or resource doesn't exist!"
        }),404
    )

@app.errorhandler(500)
def internal_server_err(err):
      return make_response(
        jsonify(
           {"message":"There's a problem! Please retry"}
        ),500
    )

@app.errorhandler(405)
def method_not_allowed(err):
    return make_response(
        jsonify(
            {"message":"The method is not allowed for this endpoint."}
        )
    )

@app.errorhandler(401)
def unauthorized(err):
    return make_response(
        jsonify(
            {"message":"You are not allowed to access this endpoint."}
        )
    )

from main.models.authors import Author
from main.models.books import Book

from main.models.users import User
@app.shell_context_processor
def make_shell_context():
    return {
        'app':app,
        'db':db,
        'Author':Author,
        'Book':Book
    }


