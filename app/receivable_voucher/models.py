from app import db, ma
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import DATE, DATETIME


class ReceivableVoucher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    receivable_desc = db.Column(db.String(100))
    chalan_no = db.Column(db.String(100))
    receivable_amount = db.Column(db.DECIMAL(10, 2))
    vat_amount = db.Column(db.DECIMAL(10, 2))
    chalan_date = Column(DATE)
    execute_date = Column(DATE)
    business_type = db.Column(db.Integer)
    created_at = Column(DATETIME)
    user_id = db.Column(db.Integer)






