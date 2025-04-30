from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db

from .models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods = ['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return 

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

        if len(email) < 4:
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
            return redirect(url_for('views.profile'))

    return render_template("signup.html")