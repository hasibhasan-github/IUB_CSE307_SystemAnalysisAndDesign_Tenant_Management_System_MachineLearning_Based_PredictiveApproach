from flask import Blueprint, render_template, request

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
            pass
        elif len(username) < 2:
            pass
        elif password != confirmPassword:
            pass
        elif len(password) < 8:
            pass
        elif len(confirmPassword) < 8:
            pass
        else:
            # Add User to Database
            pass
        
    return render_template("signup.html")