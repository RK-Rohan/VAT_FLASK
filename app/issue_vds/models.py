from app import db
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import DATE, DATETIME, FLOAT, DOUBLE


class IssueVds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vds_no = db.Column(db.String(100))
    vds_type = db.Column(db.Integer)
    entry_date = Column(DATE)
    supplier_id = db.Column(db.Integer)
    total_amount = db.Column(db.DECIMAL(10, 2))
    total_vat = db.Column(db.DECIMAL(10, 2))
    total_vds = db.Column(db.DECIMAL(10, 2))
    total_payment = db.Column(db.DECIMAL(10, 2))
    user_id = db.Column(db.Integer)


class IssueVdsLine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vds_id = db.Column(db.Integer)
    supplier_id = db.Column(db.Integer)
    invoice_no = db.Column(db.String(100))
    inv_amount = Column(DOUBLE)
    inv_date = Column(DATE)
    vat_amount = Column(DOUBLE)
    vds_amount = Column(DOUBLE)
    payment_amount = Column(DOUBLE)
    branch_name = db.Column(db.String(50))
    bank_name = db.Column(db.String(50))
    account_code = db.Column(db.String(50))
    deposit_serial = db.Column(db.String(50))
    deposit_date = Column(DATE)
    entry_date = Column(DATE)





