from flask import Flask
from .config import DevConfig
from main.utils.database import db
from flask import jsonify,make_response
from flask_migrate import Migrate



app=Flask(__name__)

app.config.from_object(DevConfig)
db.init_app(app)

migrate=Migrate(app,db)

from main.api.views import api_blueprint
app.register_blueprint(api_blueprint,url_prefix='/api')


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



from main.models.authors import Author
from main.models.books import Book
@app.shell_context_processor
def make_shell_context():
    return {
        'app':app,
        'db':db,
        'Author':Author,
        'Book':Book
    }


