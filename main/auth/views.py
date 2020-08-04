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


