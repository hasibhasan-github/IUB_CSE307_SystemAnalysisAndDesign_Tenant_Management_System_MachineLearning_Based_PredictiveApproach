from flask import Blueprint, render_template, request, flash
from flask_login import  login_required, current_user

from .models import Verification, Property, LeaseAgreement
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
    tmp = LeaseAgreement.query.filter_by(tenant_email = current_user.email).first()

    return render_template("leasedetails.html", user = current_user, tmp=tmp)

@views.route('/leasef', methods = ['GET', 'POST'])
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
    prop = Property.query.filter_by(bathrooms = current_user.id).first()
    prop1 = Property.query.filter_by(bathrooms = current_user.id).all()

    # return render_template("serviceL.html", user = current_user)
    return render_template("serviceL.html", user = current_user, prop = prop, prop1 = prop1)

@views.route('/addprop', methods = ['GET', 'POST'])
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


@views.route('/Lease')
@login_required
def Lease():
    les =LeaseAgreement.query.filter_by(landlord_email = current_user.email).all()
    tmp = LeaseAgreement.query.filter_by(landlord_email = current_user.email).first()

    return render_template("Lease.html", user = current_user, les = les, tmp = tmp)
    # return render_template("serviceL.html", user = current_user, prop = prop, prop1 = prop1)