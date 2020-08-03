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
from main.models.books import Book,BookSchema

#get all books
@api_blueprint.route('/books',methods=['GET'])
def get_all_books():
    get_all_books=Book.query.all()

    books=BookSchema(many=True).dump(get_all_books)

    return make_response(
        jsonify({
          "Success":True,
          "books":books  
        }),200
    )




#create a book
@api_blueprint.route('/books',methods=['POST'])
def create_book():
    data=request.get_json()

    new_book=Book(
        title=data['title'],
        pages=data['pages'],
        publish_year=data['publish_year'],
        description=data['description']
    )

    new_book.create()

    book=BookSchema().dump(new_book)

    return make_response(
        jsonify({
            "message":"New book created successfully!",
            "book":book

        }),201
    )

#get book by an id
@api_blueprint.route('/book/<id>',methods=['GET'])
def get_single_book(id):
    get_book=Book.query.get_or_404(id)

    book=BookSchema().dump(get_book)

    return make_response(
        jsonify({"Success":True,
                 "book":book
        }),200
    )



#update book
@api_blueprint.route('/book/<id>',methods=['PUT'])
def update_book(id):
    book_to_update=Book.query.get_or_404(id)

    data=request.get_json()

    if data['title']:
        book_to_update.title=data['title']

    if data['description']:
        book_to_update.description=data['description']


    db.session.add(book_to_update)
    db.session.commit()


    book=BookSchema().dump(book_to_update)

    return make_response(
        jsonify(
            {"message":"Book updated successfully",
             "book":book,
             "Success":True
             }
        ),200
    )

#edit book details (description)
@api_blueprint.route('/book/<id>',methods=['PATCH'])
def edit_book_details(id):
    book_to_edit=Book.query.get_or_404(id)

    data=request.get_json()

    if data['description']:
        book_to_edit.description=data['description']

    db.session.add(book_to_edit)
    db.session.commit()
    
    book=BookSchema().dump(book_to_edit)

    return make_response(
        jsonify(
            {
                "message":"Book description updated successfully",
                "book":book,
                "Success":True
            }
        ),200
    )


#delete book
@api_blueprint.route('/book/<id>',methods=['DELETE'])
def delete_book(id):
    book_to_delete=Book.query.get_or_404(id)

    book_to_delete.delete()

    book=BookSchema().dump(book_to_delete)

    return make_response(
        jsonify(
            {
                "message":"Book Deleted successfully",
                "Success":True,
                "book deleted":book
            }
        ),200

    )