from main.models.authors import Author
from main.utils.database import db
from flask import request,jsonify,make_response,Blueprint
from main.models.authors import Author,AuthorSchema
from main.models.books import Book,BookSchema

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
        }),200
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
def update_author_info(id):
    data=request.get_json()

    author_to_update=Author.query.get_or_404(id)
    
    if data['name']:
        author_to_update.name=data['name']

    if data['specialization']:
        author_to_update.specialization=data['specialization']

    db.session.add(author_to_update)
    db.session.commit()

    author=AuthorSchema().dump(author_to_update)

    return make_response(
        jsonify({
            "message":"Author's Info Updated Successfully",
            "author":author
        }),200
    )


#delete author
@api_blueprint.route('/author/<id>',methods=['DELETE'])
def delete_author(id):
    author_to_delete=Author.query.get_or_404(id)

    author_to_delete.delete()

    author=AuthorSchema().dump(author_to_delete)

    return make_response(jsonify({
        "message":"Author deleted successfully",
        "Success":True,
        "author":author
    }),200
    )

    
##############################
########BOOK VIEWS ###########
##############################


#get all books
@api_blueprint.route('/books',methods=['GET'])
def get_all_books():
    get_all_books=Book.query.all()

    books=AuthorSchema(many=True).dump(get_all_books)

    return make_response(
        jsonify({
          "Success":True,
          "books":books  
        })
    )




#create a book
@api_blueprint.route('/books',methods=['POST'])
def create_book():
    pass

#get book by an id
@api_blueprint.route('/book/<id>',methods=['GET'])
def get_single_book(id):
    pass

#update book
@api_blueprint.route('/book/<id>',methods=['PUT'])
def update_book(id):
    pass

#edit book details
@api_blueprint.route('/book/<id>',methods=['PATCH'])
def edit_book_details(id):
    pass

#delete book
@api_blueprint.route('/book/<id>',methods=['DELETE'])
def delete_book(id):
    pass