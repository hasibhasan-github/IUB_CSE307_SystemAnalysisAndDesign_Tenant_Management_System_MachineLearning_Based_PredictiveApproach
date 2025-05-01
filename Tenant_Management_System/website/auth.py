from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from flask_login import login_user, login_required, logout_user, current_user


from .models import User, Landlord

auth = Blueprint('auth', __name__)


@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data (username and password)
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if the user exists in the database
        user = User.query.filter_by(email=email).first()

        if user:
            if user.password == password :
                if user.userType == "Landlord":
                    flash("Login successful!", category="success")
                    login_user(user, remember=True)
                    return redirect(url_for('views.Lprofile'))
                else:
                    flash("Login successful!", category="success")
                    login_user(user, remember=True)
                    return redirect(url_for('views.profile'))
            else:
                flash("Invalid email or password. Please try again.", category="error")
        else:
            flash("Email doesn't exist. Please try again.", category="error")

    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))

@auth.route('/signup',  methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        gender = request.form.get('gender')
        userType = request.form.get('userType')
        contactNumber = request.form.get('contactNumber')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmPassword')

        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email already exist. Please try another.", category="error")
        elif len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 2 characters', category='error')
        elif password != confirmPassword:
            flash("Password doesn't match", category='error')
        elif len(password) < 7:
            flash('Password must be greater than 8 characters', category='error')
        elif len(confirmPassword) < 7:
            flash('ConfirmPassword must be greater than 8 characters', category='error')
        elif len(contactNumber) <= 10:
            flash('contactNumber must be greater than 10 characters', category='error')
        else:
            # Add User to Database

            if userType == "Landlord":
                new_user = Landlord(
                    email=email,        # Replace with the user's email
                    password=password,          # Replace with a hashed password
                    username=username,              # Replace with the user's username
                    gender=gender,                       # Replace with gender
                    contactNumber=contactNumber,         # Replace with the user's contact number
                    userType=userType)                 # Replace with the user's type (e.g., "Tenant", "Admin"
                db.session.add(new_user)
                db.session.commit()
                new_user1 = User(
                    email=email,        # Replace with the user's email
                    password=password,          # Replace with a hashed password
                    username=username,              # Replace with the user's username
                    gender=gender,                       # Replace with gender
                    contactNumber=contactNumber,         # Replace with the user's contact number
                    userType=userType)                 # Replace with the user's type (e.g., "Tenant", "Admin"
                db.session.add(new_user1)
                db.session.commit()
                flash('Registration Successful', category='success')
                # login_user(user, remember=True)
                return redirect(url_for('views.home'))
                pass
            else:
                new_user = User(
                    email=email,        # Replace with the user's email
                    password=password,          # Replace with a hashed password
                    username=username,              # Replace with the user's username
                    gender=gender,                       # Replace with gender
                    contactNumber=contactNumber,         # Replace with the user's contact number
                    userType=userType)                 # Replace with the user's type (e.g., "Tenant", "Admin"
                db.session.add(new_user)
                db.session.commit()
                flash('Registration Successful', category='success')
                # login_user(user, remember=True)
                return redirect(url_for('views.home'))

    return render_template("signup.html")