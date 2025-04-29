from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template("base.html")

@auth.route('/logout')
def logout():
    return 

@auth.route('/signup')
def signup():
    return 