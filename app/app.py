from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
csrf = CSRFProtect()
ma = Marshmallow()


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
    ma.init_app(app)

    # Import models file
    from auth.models import Users

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

    from purchase import purchase as purchase_blueprint
    app.register_blueprint(purchase_blueprint)

    from sales import sales as sales_blueprint
    app.register_blueprint(sales_blueprint)

    from issue_vds import issue_vds as issue_vds_blueprint
    app.register_blueprint(issue_vds_blueprint)

    from receive_vds import receive_vds as receive_vds_blueprint
    app.register_blueprint(receive_vds_blueprint)

    from reports import reports as reports_blueprint
    app.register_blueprint(reports_blueprint)

    from treasury_chalan import treasury_chalan as treasury_chalan_blueprint
    app.register_blueprint(treasury_chalan_blueprint)


    return app
