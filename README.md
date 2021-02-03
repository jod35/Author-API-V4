# Author API V4
This is the improved and last version of the CRUD AuthorApi I created a while ago. I summarises most concepts I learned while building the recent versions. It includes JWT Authentication.


### Users And Routes
To access book and author resources, You need to add the prefix ` /api ` to the root URL
For example, ` GET http://authoapiv4.herokuapp.com/api/authors ` to get a list of users

### Get authorization to access resources
To access the API, you will require to get an API Key.
Visit `https://authoapiv4.herokuapp.com/auth/signup ` to create an account
Once created visit `https://authoapiv4.herokuapp.com/auth/login` to get an access token


| ROUTE | METHOD  | DESCRIPTION |
|-------|---------|-------------|
| /authors/ | GET    | Get all authors alongside their books |
| /author/id | GET   | Get an author with an id|
| /authors/ | POST  | create a new author |
| /author/id | PUT   | Update info for an author with an id |
| /author/id | DELETE | Delete an author with an id |  
| /books/    | GET   | Get all the books |
| /book/id   | GET   | Get a book with an id |
| /books/    | POST  | Create a new book | 
| /book/id   | PUT  | Update a book with a given id |
| /book/id   | PATCH  | Edit a book's description    |
| /book/id   | DELETE | Delete a book with a given id |


## Built With
- Flask (web framework)
- Flask-Marshmallow (Object Serialization and Deserialization)
- Flask-SQLAlchemy (Object Relational Mapper for Flask and relational databases)
- PyMySQL (Database Driver for MySQL and Python)
- MySQL (An Open Source relational database)


## Author
[Ssali Jonathan(Jod35)](https://github.com/jod35)
