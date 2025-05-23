from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import pymysql  # Only needed if using PyMySQL for MySQL connection
from flask_login import LoginManager

db = SQLAlchemy()

DB_NAME = "tenant_management"  # Update this to your MySQL database name

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'DHFGHJASDVFHGFHVCDCDJU153'
    
    # MySQL connection URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@localhost/' + DB_NAME
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking

    db.init_app(app)


    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import (
        User, Verification, LeaseAgreement, MaintenanceRequest,
        Rent, Property, ServiceProvider, ServiceBill, Notification
    )

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    # This ensures that the database and tables are created
    with app.app_context():  # Ensure we're inside the app context
        try:
            db.create_all()  # This will create all the tables defined in your models
            print("Database created successfully.")
        except Exception as e:
            print("Error creating database: ", e)
