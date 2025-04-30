from flask import Blueprint, render_template
from flask_login import  login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/home')
def homeg():
    return render_template("home.html")

@views.route('/explore')
def explore():
    return render_template("explore.html")

# Profile Templates Route Tenant

@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user = current_user)

@views.route('/info')
@login_required
def info():
    return render_template("info.html", user = current_user)

@views.route('/report')
@login_required
def report():
    return render_template("report.html", user = current_user)

@views.route('/noti')
@login_required
def noti():
    return render_template("noti.html", user = current_user)

@views.route('/service')
@login_required
def service():
    return render_template("service.html", user = current_user)

@views.route('/pay')
@login_required
def pay():
    return render_template("pay.html", user = current_user)

@views.route('/pred')
@login_required
def pred():
    return render_template("pred.html", user = current_user)

# Profile Templates Route