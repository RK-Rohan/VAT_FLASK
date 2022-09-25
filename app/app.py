from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    # Configure SQLAlchemy Connection
    app.config['SECRET_KEY'] = 'f5sdf43sd4cds5vf2sd154fsd3'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/bmit_vat_service'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    app.static_folder = 'static'

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Import models file
    from auth.models import Users
    from company.models import Company

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    # Import Blueprint and Register
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from dashboard import dashboard as dashboard_blueprint
    app.register_blueprint(dashboard_blueprint)

    from company import company as company_blueprint
    app.register_blueprint(company_blueprint)

    return app
