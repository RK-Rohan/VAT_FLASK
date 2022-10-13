from app import db
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import DATE, DATETIME


class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    p_invoice_no = db.Column(db.String(100))
    purchase_type = db.Column(db.Integer)
    lc_date = Column(DATE)
    lc_no = db.Column(db.String(100))
    challan_date = Column(DATE)
    total_vds = db.Column(db.DECIMAL(10, 2))
    grand_total = db.Column(db.DECIMAL(10, 2))
    supplier_id = db.Column(db.Integer)
    total_tax = db.Column(db.DECIMAL(10, 2))
    vendor_invoice = db.Column(db.String(255))
    custom_house = db.Column(db.String(255))
    country_origin = db.Column(db.String(255))
    boe_item_no = db.Column(db.Integer)
    data_source = db.Column(db.String(155))
    cpc_code_id = db.Column(db.String(255))
    entry_date = Column(DATETIME)
    notes = db.Column(db.String(200))
    user_id = db.Column(db.Integer)

