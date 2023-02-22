from app import db, ma
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import DATE, DATETIME


class TreasuryChalan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    t_chalan_no = db.Column(db.String(100))
    t_bank = db.Column(db.String(100))
    t_branch = db.Column(db.String(100))
    t_account_code = db.Column(db.String(100))
    t_amount = db.Column(db.DECIMAL(10, 2))
    t_date = Column(DATE)
    execute_date = Column(DATE)
    t_type = db.Column(db.Integer)
    business_type = db.Column(db.Integer)
    created_at = Column(DATETIME)
    user_id = db.Column(db.Integer)






