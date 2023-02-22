from app import db, ma
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import DATE, DATETIME


class PayableMushak(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pay_type = db.Column(db.Integer)
    pay_date = Column(DATE)
    pay_amount = db.Column(db.DECIMAL(10, 2))
    business_type = db.Column(db.Integer)
    created_at = Column(DATETIME)
    user_id = db.Column(db.Integer)






