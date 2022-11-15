from app import db, ma
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import DATE, DATETIME, FLOAT, DOUBLE


class OpeningBalance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    opening_vat = db.Column(db.DECIMAL(10, 2))
    opening_sd = db.Column(db.DECIMAL(10, 2))
    closing_date = Column(DATE)
    created_at = Column(DATETIME)




