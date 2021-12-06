
from app  import db
class users(db.Model):
   id = db.Column('Id', db.Integer, primary_key = True)
   username = db.Column(db.String(100))
   nickname = db.Column(db.String(100))
   password = db.Column(db.Text())
   ava = db.Column(db.Text())
   email= db.Column(db.Text())


def __init__(self,  username, password, ava,email):
   self. username =  username
   self.nickname = nickname
   self.password = password
   self.ava = ava
   self.email = email