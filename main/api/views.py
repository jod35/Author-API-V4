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
    all_authors=Author.query.all()

    author_schema=AuthorSchema(many=True)

    authors=author_schema.dump(all_authors)

    message="authors"

    return make_response(
        jsonify({
            "message":message,
            "authors":authors
        }),200
    )

#get an author with an ID
@api_blueprint.route('/author/<id>',methods=['GET'])
def get_single_author(id):
    single_author=Author.query.get_or_404(id)

    author=AuthorSchema().dump(single_author)

    return make_response(
        jsonify({
            "Success":True,
            "Author":author
        })
    )
   

#create an new author
@api_blueprint.route('/authors',methods=['POST'])
def create_new_author():
    data=request.get_json() #getting data in JSON format

    new_author=Author(
        name=data['name'],
        email=data['email'],
        specialization=data['specialization']
    )
    
    password=data['password']

    new_author.hash_password(password)

    new_author.create() #save the new author to db

    author=AuthorSchema().dump(new_author)

    return make_response(
        jsonify(
            {
                "success":True,
                "message":"Author created successfully",
                "author":author
            }
        ),201
    )


#update author info
@api_blueprint.route('/author/<id>',methods=['PUT'])
def update_author_info():
    pass

#delete author
@api_blueprint.route('/author/<id>')
def delete_author():
    pass
