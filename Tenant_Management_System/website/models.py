from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Coloumn(db.Integer, primary_key = True)
    email = db.Coloumn(db.String(30), unique = True)
    password = db.Coloumn(db.String(30))