from app import db


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
