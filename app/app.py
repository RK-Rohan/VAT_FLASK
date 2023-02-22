from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # Configure SQLAlchemy Connection
    app.config['SECRET_KEY'] = 'seCREtKeY'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/bmit_vat_service'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    app.static_folder = 'static'

    db.init_app(app)

    # Import Blueprint and Register
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
