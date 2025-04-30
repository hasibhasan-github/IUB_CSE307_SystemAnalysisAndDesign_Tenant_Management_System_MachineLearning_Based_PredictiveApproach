from flask import Blueprint, render_template, request, flash
from flask_login import  login_required, current_user

from .models import Verification
from . import db

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
    verify = Verification.query.filter_by(user_id = current_user.id).first()
    if request.method == 'POST':
        nid_number = request.form.get("NId")
        name = request.form.get("name")
        gender = request.form.get("gender")
        email = request.form.get("email")
        contact_number = request.form.get("contactNo")
        dob = request.form.get("dob")
        user_type = request.form.get("usertype")
        address = request.form.get("add")
        verification_status = "Pending"
        user_id = request.form.get("id")
    
        new_verification = Verification(
                nid_number=nid_number,
                name=name,
                gender=gender,
                email=email,
                contact_number=contact_number,
                dob=dob,  # Ensure 'dob' is in the correct format (datetime.date)
                user_type=user_type,
                address=address,
                verification_status=verification_status,
                user_id=user_id  # This is the foreign key linking to the User model
            )
        db.session.add(new_verification)
        db.session.commit() 
        flash("Verification Request Successful!", category="success")
        return render_template("info.html", user = current_user, verify = verify)

    return render_template("info.html", user = current_user, verify = verify)

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