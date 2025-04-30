from flask import Blueprint, render_template, request
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

@views.route('/info', methods = ['GET', 'POST'])
@login_required
def info():
    nid_number = request.form.get("NId")
    dob = request.form.get("")
    verification_status = request.form.get("")
    user_id = request.form.get("")
    name = request.form.get("name")
    gender = request.form.get("gender")
    email = request.form.get("email")
    contact_number = request.form.get("")
    user_type = request.form.get("")
    address = request.form.get("")

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