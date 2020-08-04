from main.utils.database import db
from werkzeug.security import generate_password_hash,check_password_hash
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(25),unique=True)
    email=db.Column(db.String(80),unique=True)
    passwd_hash=db.Column(db.Text)

    def __repr__(self):
        return f'User <{self.username}>'

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

from main.utils.logins import login_manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class UserSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model=User
        sqla_session=db.session

    id=fields.Integer(dump_only=True)
    username=fields.String(required=True)
    email=fields.String(required=True)
    