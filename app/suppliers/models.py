from app import db


class Suppliers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplier_name = db.Column(db.String(100))
    email_address = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
    country_id = db.Column(db.String(100))
    supplier_type = db.Column(db.String(100))
    supplier_address = db.Column(db.String(100))
    supplier_bin = db.Column(db.String(100))
    supplier_tin = db.Column(db.String(100))
