from main.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from datetime import datetime


class Book(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    title=db.Column(db.String(255),nullable=False)
    uploaded=db.Column(db.DateTime(),default=datetime.utcnow)
    pages=db.Column(db.Integer,nullable=False)
    publish_year=db.Column(db.String(4),nullable=False)
    description=db.Column(db.Text())
    author_id=db.Column(db.Integer(),db.ForeignKey('author.id'))

    def __repr__(self):
        return f'Book <{self.title}>'

    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class BookSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model=Book
        sqla_session=db.session


    id=fields.Integer()
    title=fields.String(required=True)
    pages=fields.Integer(required=True)
    publish_year=fields.String(required=True)
    description=fields.String(required=True)




