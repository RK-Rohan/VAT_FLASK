from app import db
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import TINYINT, YEAR


class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100))
    item_type = db.Column(db.String(100))
    hs_code = db.Column(db.String(100))
    hs_code_id = db.Column(db.String(100))
    calculate_year = db.Column(db.String(100))
    unit_id = db.Column(db.String(100))
    stock_status = db.Column(db.String(100))
    status = db.Column(db.String(100))


class HSCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    heading = db.Column(db.String(100))
    hs_code = db.Column(db.String(100))
    description = db.Column(db.String(255))
    cd = db.Column(db.DECIMAL(10, 2))
    sd = db.Column(db.DECIMAL(10, 2))
    vat = db.Column(db.DECIMAL(10, 2))
    ait = db.Column(db.DECIMAL(10, 2))
    rd = db.Column(db.DECIMAL(10, 2))
    at = db.Column(db.DECIMAL(10, 2))
    tti = db.Column(db.DECIMAL(10, 2))
    schedule = db.Column(db.String(255))
    vat_type = Column(TINYINT)
    type = Column(TINYINT)
    year_start = db.Column(db.Date)
    year_end = db.Column(db.Date)
    calculate_year = Column(YEAR)
