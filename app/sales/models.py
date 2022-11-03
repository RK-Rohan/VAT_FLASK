from app import db, ma
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import DATE, DATETIME, FLOAT, DOUBLE


class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer)
    sale_center_id = db.Column(db.Integer)
    sales_transfer_id = db.Column(db.Integer)
    sale_date = Column(DATE)
    sales_invoice = db.Column(db.String(100))
    vehicle_info = db.Column(db.String(100))
    destination = db.Column(db.String(100))
    sales_challan = db.Column(db.String(100))
    entry_date = Column(DATETIME)
    sales_type = db.Column(db.Integer)
    trans_type = db.Column(db.Integer)
    total_discount = db.Column(db.DECIMAL(10, 2))
    total_sd = db.Column(db.DECIMAL(10, 2))
    total_vat = db.Column(db.DECIMAL(10, 2))
    grand_total = db.Column(db.DECIMAL(10, 2))
    notes = db.Column(db.String(200))
    user_id = db.Column(db.Integer)


class SalesSchema(ma.Schema):
    class Meta:
        fields = (
            "id", "sales_invoice", "sale_date", "customer_id", "total_sd", "total_vat", "grand_total",
            "entry_date", "user_id"
        )


class SalesLine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer)
    hs_code_id = db.Column(db.Integer)
    sales_id = db.Column(db.Integer)
    qty = Column(FLOAT)
    rate = db.Column(db.DECIMAL(10, 2))
    rate_value = db.Column(db.DECIMAL(10, 2))
    discount_percent = db.Column(db.DECIMAL(10, 2))
    discount_amount = db.Column(db.DECIMAL(10, 2))
    value_after_discount = db.Column(db.DECIMAL(10, 2))
    sd_percent = db.Column(db.DECIMAL(10, 2))
    sd_amount = db.Column(db.DECIMAL(10, 2))
    vatable_value = db.Column(db.DECIMAL(10, 2))
    vat_type = db.Column(db.String(100))
    vat_percent = db.Column(db.DECIMAL(10, 2))
    vat_amount = db.Column(db.DECIMAL(10, 2))
    vds = db.Column(db.String(100))
    sales_date = Column(DATE)
    sub_total = db.Column(db.DECIMAL(10, 2))




