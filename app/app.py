from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)

    # Configure SQLAlchemy Connection
    app.config['SECRET_KEY'] = 'seCREtKeY'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/bmit_vat_service'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    app.static_folder = 'static'

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)

    # Import models file
    from auth.models import Users
    from company.models import Company
    from units.models import Units
    # from customers.models import Customers

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

    from units import units as units_blueprint
    app.register_blueprint(units_blueprint)

    from customers import customers as customers_blueprint
    app.register_blueprint(customers_blueprint)

    from suppliers import suppliers as suppliers_blueprint
    app.register_blueprint(suppliers_blueprint)

    from items import items as items_blueprint
    app.register_blueprint(items_blueprint)

    return app
