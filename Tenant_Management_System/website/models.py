from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Coloumn(db.Integer, primary_key = true)