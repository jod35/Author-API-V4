from main.utils.database import db
from werkzeug.security import generate_password_hash,check_password_hash

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

