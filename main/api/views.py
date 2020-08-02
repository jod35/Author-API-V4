from main.models.authors import Author
from main.utils.database import db
from flask import request,jsonify,make_response,Blueprint


api_blueprint=Blueprint('api_bp',__name__)

@api_blueprint.route('/')
def hello():
    return make_response(
        jsonify({"message":"Hello"})
    )