# Author API V4
This is the improved and last version of the CRUD AuthorApi I created a while ago. I summarises most concepts I learned while building the recent versions. It includes JWT Authentication.

## The Endpoints

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