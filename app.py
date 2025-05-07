from flask import Flask

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

from flask import Blueprint, render_template, request, flash
from flask_login import  login_required, current_user

from .Tenant_Management_System.website.models import Verification, Property, LeaseAgreement, User, Landlord
from . import db

from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from flask_login import login_user, login_required, logout_user, current_user

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/home')
def homeg():
    return render_template("home.html")

@app.route('/explore')
def explore():
    return render_template("explore.html")

# Profile Templates Route Tenant

@app.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user = current_user)

@app.route('/info', methods = ['GET', 'POST'])
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

@app.route('/report')
@login_required
def report():
    return render_template("report.html", user = current_user)

@app.route('/report1')
@login_required
def report1():
    return render_template("report1.html", user = current_user)

@app.route('/noti')
@login_required
def noti():
    return render_template("noti.html", user = current_user)

@app.route('/service')
@login_required
def service():
    return render_template("service.html", user = current_user)

@app.route('/pay')
@login_required
def pay():
    return render_template("pay.html", user = current_user)

@app.route('/pred')
@login_required
def pred():
    return render_template("pred.html", user = current_user)

@app.route('/lease')
@login_required
def lease():
    tmp = LeaseAgreement.query.filter_by(tenant_email = current_user.email).first()

    return render_template("leasedetails.html", user = current_user, tmp=tmp)

@app.route('/leasef', methods = ['GET', 'POST'])
@login_required
def leasef():
    tmp = LeaseAgreement.query.filter_by(landlord_email = current_user.email).first()
    les =LeaseAgreement.query.filter_by(landlord_email = current_user.email).all()
    if request.method == 'POST':
        tenant_name = request.form.get("tenantName")
        tenant_email = request.form.get("tenantEmail")
        tenant_phone_number = request.form.get("tenantPhone")
        landlord_name = current_user.username
        landlord_email = current_user.email
        landlord_phone_number = current_user.contactNumber
        monthly_rent = request.form.get("monthlyRent")
        security_deposit = request.form.get("securityDeposit") #monthlyRent
        lease_start_date = request.form.get("leaseStart")
        lease_end_date = request.form.get("leaseEnd") 

        new_lease_agreement = LeaseAgreement(
        tenant_name=tenant_name,
        tenant_email=tenant_email,
        tenant_phone_number=tenant_phone_number,
        landlord_name=landlord_name,
        landlord_email=landlord_email,
        landlord_phone_number=landlord_phone_number,
        monthly_rent=monthly_rent,
        security_deposit=security_deposit,
        lease_start_date=lease_start_date,
        lease_end_date=lease_end_date,)

        db.session.add(new_lease_agreement)
        db.session.commit()

        return render_template("Lease.html", user = current_user, les = les, tmp = tmp)


    return render_template("leaseform.html", user = current_user)

@app.route('/mainform')
@login_required
def mainform():
    return render_template("mainform.html", user = current_user)

# Profile Templates Route



# Profile Templates Route Landlord

@app.route('/Lprofile')
@login_required
def Lprofile():
    return render_template("Lprofile.html", user = current_user)

@app.route('/info1', methods = ['GET', 'POST'])
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


@app.route('/Lreport')
@login_required
def Lreport():
    return render_template("Lreport.html", user = current_user)

@app.route('/Lreport1')
@login_required
def Lreport1():
    return render_template("Lreport1.html", user = current_user)

@app.route('/noti1')
@login_required
def noti1():
    return render_template("noti1.html", user = current_user)


@app.route('/serviceL')
@login_required
def serviceL():
    prop = Property.query.filter_by(bathrooms = current_user.id).first()
    prop1 = Property.query.filter_by(bathrooms = current_user.id).all()

    # return render_template("serviceL.html", user = current_user)
    return render_template("serviceL.html", user = current_user, prop = prop, prop1 = prop1)

@app.route('/addprop', methods = ['GET', 'POST'])
@login_required
def addprop():
    prop = Property.query.filter_by(bathrooms = current_user.id).first()
    prop1 = Property.query.filter_by(bathrooms = current_user.id).all()
    
    if request.method == 'POST':
        property_name = request.form.get("propertyName")
        property_description = request.form.get("propertyDescription")
        property_location = request.form.get("propertyLocation")
        property_rent = request.form.get("propertyRent")
        property_type = request.form.get("propertyType")
        bedrooms = request.form.get("bedrooms")
        bathrooms = current_user.id
        property_size = request.form.get("propertySize")
        available_from = request.form.get("availableFrom")
        lease_terms = request.form.get("leaseTerms")

        new_property = Property(
        property_name=property_name,
        property_description=property_description,
        property_location=property_location,
        property_rent=property_rent,
        property_type=property_type,
        bedrooms=bedrooms,
        bathrooms=bathrooms,
        property_size=property_size,
        available_from=available_from,
        lease_terms=lease_terms,
                         # Assuming current_user is the landlord
)       
        db.session.add(new_property)
        db.session.commit()
        return render_template("serviceL.html", user = current_user, prop = prop, prop1 = prop1)

    return render_template("addprop.html", user = current_user, prop = prop, prop1 = prop1)


@app.route('/Lease')
@login_required
def Lease():
    les =LeaseAgreement.query.filter_by(landlord_email = current_user.email).all()
    tmp = LeaseAgreement.query.filter_by(landlord_email = current_user.email).first()

    return render_template("Lease.html", user = current_user, les = les, tmp = tmp)
    # return render_template("serviceL.html", user = current_user, prop = prop, prop1 = prop1)



@app.route('/login', methods = ['GET', 'POST'])
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

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))

@app.route('/signup',  methods = ['GET', 'POST'])
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

if __name__ == "__main__":
    app.run()
