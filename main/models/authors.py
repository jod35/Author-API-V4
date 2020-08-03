from main.utils.database import db
from werkzeug.security import generate_password_hash,check_password_hash
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class Author(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255),nullable=False)
    email=db.Column(db.String(255),unique=True)
    specialization=db.Column(db.String(255))
    passwd_hash=db.Column(db.Text)

    from main.models.books import Book

    books=db.relationship('Book',backref='author',lazy=True)

    def __repr__(self):
        return f'Author <{self.name}>'

    #creating an author

    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def hash_password(self,password):
        self.passwd_hash=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.passwd_hash,password)



##################################
##### OUTPUT SCHEMA ##############
##################################

class AuthorSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model=Author
        sqla_session=db.session

    id=fields.Integer()
    name=fields.String()
    email=fields.String()
    specialization=fields.String()
