from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/home')
def homeg():
    return render_template("home.html")

@views.route('/explore')
def explore():
    return render_template("base.html")

# Profile Templates Route

@views.route('/profile')
def profile():
    return render_template("profile.html")

@views.route('/info')
def info():
    return render_template("info.html")

@views.route('/report')
def report():
    return render_template("report.html")

@views.route('/noti')
def noti():
    return render_template("noti.html")

@views.route('/service')
def service():
    return render_template("service.html")

@views.route('/pay')
def pay():
    return render_template("pay.html")

@views.route('/pred')
def pred():
    return render_template("pred.html")