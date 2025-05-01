from . import db
from flask_login import UserMixin
from sqlalchemy.orm import relationship

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(30), unique = True,  nullable=False)
    password = db.Column(db.String(30),  nullable=False)
    username = db.Column(db.String(30),  nullable=False)
    gender = db.Column(db.String(10))
    contactNumber = db.Column(db.String(11),  nullable=False)
    userType = db.Column(db.String(10))

class Landlord(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(30), unique = True,  nullable=False)
    password = db.Column(db.String(30),  nullable=False)
    username = db.Column(db.String(30),  nullable=False)
    gender = db.Column(db.String(10))
    contactNumber = db.Column(db.String(11),  nullable=False)
    userType = db.Column(db.String(10))
        

class Verification(db.Model):
    nid_number = db.Column(db.String(20), primary_key=True, unique=True, nullable=False)  # NID as Primary Key
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)
    dob = db.Column(db.Date, nullable=False)  # Store date of birth as a date field
    user_type = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    verification_status = db.Column(db.String(20), default='Not Verified', nullable=False)


    # Reference to User (foreign key)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Define the relationship between Verification and User
    user = db.relationship('User', backref=db.backref('verifications', lazy=True))


class LeaseAgreement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    # Tenant Details
    tenant_name = db.Column(db.String(100), nullable=False)
    tenant_email = db.Column(db.String(120), unique=True, nullable=False)
    tenant_phone_number = db.Column(db.String(15), nullable=False)
    
    # Landlord Details
    landlord_name = db.Column(db.String(100), nullable=False)
    landlord_email = db.Column(db.String(120), unique=True, nullable=False)
    landlord_phone_number = db.Column(db.String(15), nullable=False)
    
    # Lease Details
    monthly_rent = db.Column(db.Float, nullable=False)
    security_deposit = db.Column(db.Float, nullable=False)
    lease_start_date = db.Column(db.Date, nullable=False)  # Store date as date type
    lease_end_date = db.Column(db.Date, nullable=False)  # Store date as date type


class MaintenanceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    # Tenant Information
    tenant_name = db.Column(db.String(100), nullable=False)
    tenant_email = db.Column(db.String(120), nullable=False)
    tenant_phone = db.Column(db.String(15), nullable=False)
    
    # Maintenance Service Details
    issue_type = db.Column(db.String(50), nullable=False)

class Rent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    # Rent Information
    tenant_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Link to User (Tenant)
    landlord_id = db.Column(db.Integer, db.ForeignKey('landlord.id'), nullable=False)  # Link to User (Tenant)
    month = db.Column(db.String(20), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rent_status = db.Column(db.String(20), default='Due', nullable=False)

    tenant = db.relationship('User', backref=db.backref('rent', lazy=True))

    landlord = db.relationship('Landlord', backref=db.backref('rent', lazy=True))




class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    # Property Information
    property_name = db.Column(db.String(100), nullable=False)
    property_description = db.Column(db.Text, nullable=False)
    property_location = db.Column(db.String(200), nullable=False)
    property_rent = db.Column(db.Float, nullable=False)
    property_type = db.Column(db.String(50), nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    property_size = db.Column(db.Integer, nullable=False)  # Size in sq. ft.  # Image URL or file path

    # Property Availability and Lease Terms
    available_from = db.Column(db.Date, nullable=False)
    lease_terms = db.Column(db.Text, nullable=False)

class ServiceProvider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)

class ServiceBill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    service_provider_id = db.Column(db.Integer, db.ForeignKey('service_provider.id'), nullable=False)

    # Relationship to the ServiceProvider model
    service_provider = db.relationship('ServiceProvider', backref=db.backref('bills', lazy=True))  


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255), nullable=False)

