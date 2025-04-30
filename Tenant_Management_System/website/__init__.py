from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()

DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'DHFGHJASDVFHGFHVCDCDJU153'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///path/to/database.db'
    db.init_app(app)

    from .views import views
    from .auth import auth

    from .models import User, Verification, LeaseAgreement, MaintenanceRequest, Rent, Property, ServiceProvider, ServiceBill, Notification

    create_database()

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("created")
