from app import db


class Customers(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100))
    email_address = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
    country_id = db.Column(db.String(100))
    customer_type = db.Column(db.String(100))
    customer_address = db.Column(db.String(100))
    shipping_address = db.Column(db.String(100))
    shipping_country = db.Column(db.String(100))
    customer_bin = db.Column(db.String(100))
    customer_tin = db.Column(db.String(100))
