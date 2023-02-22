from app import db


class Units(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unit_name = db.Column(db.String(100))
    short_name = db.Column(db.String(50))

