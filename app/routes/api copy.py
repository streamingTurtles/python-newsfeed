from flask import Blueprint
from app.models import User
from app.db import get_db
# lesson 4 added
# from flask import Blueprint, request
# lesson 4 update more - comment out above the flask import to allow the use of more data for JSON that includes the ID of a new user updated import below
from flask import Blueprint, request, jsonify



bp = Blueprint('api', __name__, url_prefix='/api')



@bp.route('/users', methods=['POST'])
def signup():
  data = request.get_json()
  db = get_db()

  # create a new user
  newUser = User(
    username = data['username'],
    email = data['email'],
    password = data['password']
  )

  # save in database
  db.add(newUser)
  db.commit()
  return jsonify(id = newUser.id)






