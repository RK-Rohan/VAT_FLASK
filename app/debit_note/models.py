from app import db
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import DATE, DATETIME, FLOAT, DOUBLE


class DebitNote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    debit_note_no = db.Column(db.String(100))
    debit_note_type = db.Column(db.Integer)
    dn_issue_date = Column(DATE)
    purchase_id = db.Column(db.Integer)
    supplier_id = db.Column(db.Integer)
    vehicle_info = db.Column(db.String(100))
    total_amount = db.Column(db.DECIMAL(10, 2))
    total_vat = db.Column(db.DECIMAL(10, 2))
    total_sd = db.Column(db.DECIMAL(10, 2))
    note = db.Column(db.String(255))
    created_at = Column(DATETIME)
    user_id = db.Column(db.Integer)


class DebitNoteLine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    debit_note_id = db.Column(db.Integer)
    item_id = db.Column(db.Integer)
    qty = db.Column(db.Integer)
    rate = db.Column(db.DECIMAL(10, 2))
    p_amount = db.Column(db.DECIMAL(10, 2))
    p_vat_percent = db.Column(db.DECIMAL(10, 2))
    p_vat_amount = db.Column(db.DECIMAL(10, 2))
    p_sd = db.Column(db.DECIMAL(10, 2))
    return_qty = db.Column(db.Integer)
    return_amount = db.Column(db.DECIMAL(10, 2))
    return_vat = db.Column(db.DECIMAL(10, 2))
    return_sd = db.Column(db.DECIMAL(10, 2))
    entry_date = Column(DATE)
    created_at = Column(DATETIME)





