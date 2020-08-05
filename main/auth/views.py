######################################
##### AUTHENTICATION VIEWS ###########
######################################

from flask import jsonify,Blueprint,request,make_response
from main.models.users import User,UserSchema
from main.utils.database import db
from flask_jwt_extended import create_access_token,jwt_required


auth_blueprint=Blueprint('auth_bp',__name__)

#creation of an account
@auth_blueprint.route('/signup',methods=['POST'])
def create_account():
    data=request.get_json()

    new_user=User(
        username=data['username'],
        email=data['email'],
    
    )
    new_user.hash_password(data['password'])

    new_user.create()

    user=UserSchema().dump(new_user)

    return make_response(
        jsonify({
            "message":"Account Created Successfully",
            "user":user
        })
    )


#login user
@auth_blueprint.route('/login',methods=['POST'])
def login():
    data=request.get_json()

    username=data['username']
    password=data['password']

    user=User.query.filter_by(username=username).first()

    if not user:
        return make_response(
            jsonify({
                "message":"No such user exists"
            }),404
        )

    if user and user.check_password(password):
        access_token=create_access_token(identity=data['username'])

        message="Logged In as {}".format(data['username'])

        return make_response(
            jsonify(
                {"message":message,
                 "Success":True,
                 "access_token":access_token}
            )
        )





