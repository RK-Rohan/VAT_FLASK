from app import db
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import DATE, DATETIME, FLOAT, DOUBLE
from sqlalchemy_serializer import SerializerMixin


class Sales(db.Model, SerializerMixin):
    serialize_only = ('non_sqlalchemy_field', 'id')
    serialize_rules = ()
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer)
    sale_center_id = db.Column(db.Integer)
    sales_transfer_id = db.Column(db.Integer)
    sale_date = Column(DATE)
    sales_invoice = db.Column(db.String(100))
    vehicle_info = db.Column(db.String(100))
    destination = db.Column(db.String(100))
    sales_challan = db.Column(db.String(100))
    challan_date = Column(DATETIME)
    sales_type = db.Column(db.Integer)
    trans_type = db.Column(db.Integer)
    total_discount = db.Column(db.DECIMAL(10, 2))
    total_sd = db.Column(db.DECIMAL(10, 2))
    total_vat = db.Column(db.DECIMAL(10, 2))
    grand_total = db.Column(db.DECIMAL(10, 2))
    notes = db.Column(db.String(200))
    user_id = db.Column(db.Integer)


class SalesLine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer)
    hs_code_id = db.Column(db.Integer)
    sales_id = db.Column(db.Integer)
    qty = Column(FLOAT)
    rate = Column(DOUBLE)
    rate_value = Column(DOUBLE)
    discount_percent = Column(DOUBLE)
    discount_amount = Column(DOUBLE)
    value_after_discount = Column(DOUBLE)
    sd_percent = Column(DOUBLE)
    sd_amount = Column(DOUBLE)
    vatable_value = Column(DOUBLE)
    vat_type = db.Column(db.String(100))
    vat_percent = Column(DOUBLE)
    vat_amount = Column(DOUBLE)
    vds = db.Column(db.String(100))
    sales_date = Column(DATE)
    sub_total = Column(DOUBLE)




