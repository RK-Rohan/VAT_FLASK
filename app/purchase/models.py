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


class Purchase_line(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer)
    hs_code_id = db.Column(db.Integer)
    purchase_id = db.Column(db.Integer)
    qty = Column(FLOAT)
    rate = Column(DOUBLE)
    rate_value = Column(DOUBLE)
    vatable_value = Column(DOUBLE)
    vat_percent = Column(DOUBLE)
    vat_amount = Column(DOUBLE)
    cd_percent = Column(DOUBLE)
    cd_amount = Column(DOUBLE)
    sd_percent = Column(DOUBLE)
    sd_amount = Column(DOUBLE)
    rd_percent = Column(DOUBLE)
    rd_amount = Column(DOUBLE)
    at_amount = Column(DOUBLE)
    ait_amount = Column(DOUBLE)
    tti_percent = Column(DOUBLE)
    tti_amount = Column(DOUBLE)
    vat_type = db.Column(db.String(100))
    vds = db.Column(db.String(100))
    rebate = db.Column(db.String(100))
    purchase_date = Column(DATE)
    entry_date = Column(DATETIME)
    sub_total = Column(DOUBLE)
    grand_total = Column(DOUBLE)




