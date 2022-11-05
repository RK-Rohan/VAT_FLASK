from app import db, ma
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import DATE, DATETIME, FLOAT, DOUBLE
from sqlalchemy_serializer import SerializerMixin


class Purchase(db.Model, SerializerMixin):
    serialize_only = ('non_sqlalchemy_field', 'id')
    serialize_rules = ()
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


class PurchaseSchema(ma.Schema):
    class Meta:
        fields = (
            "id", "p_invoice_no", "challan_date", "supplier_id", "total_vds", "total_tax", "grand_total",
            "entry_date", "user_id"
        )


class PurchaseLine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer)
    hs_code_id = db.Column(db.Integer)
    purchase_id = db.Column(db.Integer)
    qty = Column(FLOAT)
    rate = db.Column(db.DECIMAL(10, 2))
    rate_value = db.Column(db.DECIMAL(10, 2))
    vatable_value = db.Column(db.DECIMAL(10, 2))
    vat_percent = db.Column(db.DECIMAL(10, 2))
    vat_amount = db.Column(db.DECIMAL(10, 2))
    cd_percent = db.Column(db.DECIMAL(10, 2))
    cd_amount = db.Column(db.DECIMAL(10, 2))
    sd_percent = db.Column(db.DECIMAL(10, 2))
    sd_amount = db.Column(db.DECIMAL(10, 2))
    rd_percent = db.Column(db.DECIMAL(10, 2))
    rd_amount = db.Column(db.DECIMAL(10, 2))
    at_amount = db.Column(db.DECIMAL(10, 2))
    ait_amount = db.Column(db.DECIMAL(10, 2))
    tti_percent = db.Column(db.DECIMAL(10, 2))
    tti_amount = db.Column(db.DECIMAL(10, 2))
    vat_type = db.Column(db.String(100))
    vds = db.Column(db.String(100))
    rebate = db.Column(db.String(100))
    purchase_date = Column(DATE)
    entry_date = Column(DATETIME)
    sub_total = db.Column(db.DECIMAL(10, 2))
    grand_total = db.Column(db.DECIMAL(10, 2))




