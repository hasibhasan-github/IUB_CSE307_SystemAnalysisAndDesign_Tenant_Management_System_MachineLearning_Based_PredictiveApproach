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
        return render_template("info.html", user = current_user, ver = verify)

    return render_template("info.html", user = current_user, ver = verify)

@views.route('/report')
@login_required
def report():
    return render_template("report.html", user = current_user)

@views.route('/report1')
@login_required
def report1():
    return render_template("report1.html", user = current_user)

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

@views.route('/lease')
@login_required
def lease():
    return render_template("leasedetails.html", user = current_user)

@views.route('/leasef')
@login_required
def leasef():
    return render_template("leaseform.html", user = current_user)

@views.route('/mainform')
@login_required
def mainform():
    return render_template("mainform.html", user = current_user)

# Profile Templates Route



# Profile Templates Route Landlord

@views.route('/Lprofile')
@login_required
def Lprofile():
    return render_template("Lprofile.html", user = current_user)

@views.route('/info1', methods = ['GET', 'POST'])
@login_required
def info1():
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
        return render_template("info1.html", user = current_user, ver = verify)

    return render_template("info1.html", user = current_user, ver = verify)


@views.route('/Lreport')
@login_required
def Lreport():
    return render_template("Lreport.html", user = current_user)

@views.route('/Lreport1')
@login_required
def Lreport1():
    return render_template("Lreport1.html", user = current_user)

@views.route('/noti1')
@login_required
def noti1():
    return render_template("noti1.html", user = current_user)


@views.route('/serviceL')
@login_required
def serviceL():
    return render_template("serviceL.html", user = current_user)

@views.route('/addprop', methods = ['GET', 'POST'])
@login_required
def addprop():
    return render_template("addprop.html", user = current_user)