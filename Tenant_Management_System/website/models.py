from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Coloumn(db.Integer, primary_key = True)
    email = db.Coloumn(db.String(30), unique = True,  nullable=False)
    password = db.Coloumn(db.String(30),  nullable=False)
    username = db.Coloumn(db.String(30),  nullable=False)
    gender = db.Coloumn(db.String(10))
    contactNumber = db.Coloumn(db.String(11),  nullable=False)
    userType = db.Coloumn(db.String(10))