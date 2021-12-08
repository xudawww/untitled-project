from flask import request
from . import routes
from ..controller.jwtFilter import token_required
from ..models.user import users
from werkzeug.security import generate_password_hash


@routes.route('/register', methods=['POST'])
@token_required
def users():
    userdata = request.get_json()
    print(userdata)
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = users(username=data['username'], nickname=data['nickname'],
                     password=hashed_password, ava=data['ava'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
