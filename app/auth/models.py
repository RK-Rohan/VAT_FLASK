from flask_login import UserMixin
from app import db, login_manager


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False, index=True)
    first_name = db.Column(db.String(500))
    last_name = db.Column(db.String(500))
    email = db.Column(db.String(100), unique=True, index=True)
    password = db.Column(db.String(100))

    @classmethod
    def find_by_email(cls, email: str) -> "Users":
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_username(cls, username: str) -> "Users":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id: int) -> "Users":
        return cls.query.filter_by(id=_id).first()


@login_manager.user_loader
def user_loader(user_id):
    return Users.query.filter_by(id=user_id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = Users.query.filter_by(username=username).first()
    return user if user else None
