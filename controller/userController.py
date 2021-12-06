from ..models.user import users
from ..app import db

def addUser(user:users):
  db.session.add(user)