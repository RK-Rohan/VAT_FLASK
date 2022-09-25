from flask_login import UserMixin
from app import db


class Company(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100))
    short_name = db.Column(db.String(50))
    email_address = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
    country = db.Column(db.String(100))
    address = db.Column(db.String(100))
    invoice_logo = db.Column(db.String(100))
    bank_name = db.Column(db.String(100))
    ac_number = db.Column(db.String(100))
    branch = db.Column(db.String(100))
    business_nature = db.Column(db.String(100))
    business_economics = db.Column(db.String(100))
    vat_type = db.Column(db.String(100))
    bin_number = db.Column(db.String(100))
    tin_number = db.Column(db.String(100))
    currency = db.Column(db.String(100))
    person_name = db.Column(db.String(100))
    designation = db.Column(db.String(100))
    person_phone_number = db.Column(db.String(100))
    nid = db.Column(db.String(100))
    person_email = db.Column(db.String(100))

