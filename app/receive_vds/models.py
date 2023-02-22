from app import db
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import DATE, DATETIME, FLOAT, DOUBLE


class ReceiveVds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vds_no = db.Column(db.String(100))
    vds_type = db.Column(db.Integer)
    entry_date = Column(DATE)
    vds_certificate_no = db.Column(db.String(100))
    receive_date = Column(DATE)
    customer_id = db.Column(db.Integer)
    total_amount = db.Column(db.DECIMAL(10, 2))
    total_vat = db.Column(db.DECIMAL(10, 2))
    total_vds = db.Column(db.DECIMAL(10, 2))
    total_receive = db.Column(db.DECIMAL(10, 2))
    user_id = db.Column(db.Integer)


class ReceiveVdsLine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vds_id = db.Column(db.Integer)
    invoice_no = db.Column(db.String(100))
    customer_id = db.Column(db.Integer)
    inv_amount = db.Column(db.DECIMAL(10, 2))
    inv_date = Column(DATE)
    vat_amount = db.Column(db.DECIMAL(10, 2))
    vds_amount = db.Column(db.DECIMAL(10, 2))
    receive_amount = db.Column(db.DECIMAL(10, 2))
    branch_name = db.Column(db.String(50))
    bank_name = db.Column(db.String(50))
    account_code = db.Column(db.String(50))
    deposit_serial = db.Column(db.String(50))
    deposit_date = Column(DATE)
    entry_date = Column(DATE)





