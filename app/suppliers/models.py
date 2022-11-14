from app import db, ma


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


class SuppliersSchema(ma.Schema):
    class Meta:
        fields = (
            "id", "supplier_name", "email_address", "country_id", "supplier_type", "supplier_address", "supplier_bin",
            "supplier_tin"
        )
