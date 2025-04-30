from flask import Blueprint, render_template, request, flash

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
        contactNumber = request.form.get('contactNumber')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmPassword')

        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 2 characters', category='error')
        elif password != confirmPassword:
            flash("Password doesn't match", category='error')
        elif len(password) < 8:
            flash('Password must be greater than 8 characters', category='error')
        elif len(confirmPassword) < 8:
            flash('ConfirmPassword must be greater than 8 characters', category='error')
        else:
            # Add User to Database
            pass

    return render_template("signup.html")