from main.models.authors import Author
from main.utils.database import db
from flask import request,jsonify,make_response,Blueprint
from main.models.authors import Author,AuthorSchema


api_blueprint=Blueprint('api_bp',__name__)


#hello message on the / route
@api_blueprint.route('/')
def hello():
    return make_response(
        jsonify({"message":"Hello, Welcome to the Author Api"})
    )

###################################
######### Author end points #######
###################################

#get all authors
@api_blueprint.route('/authors',methods=['GET'])
def get_all_authors():
    pass

#get an author with an ID
@api_blueprint.route('/author/<id>',methods=['GET'])
def get_single_author():
    pass

#create an new author
@api_blueprint.route('/authors',methods=['POST'])
def create_new_author():
    pass

#update author info
@api_blueprint.route('/author/<id>',methods=['PUT'])
def update_author_info():
    pass

#delete author
@api_blueprint.route('/author/<id>')
def delete_author():
    pass
