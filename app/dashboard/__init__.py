from flask import Blueprint

dashboard = Blueprint('dashboard', __name__)


from dashboard import routes
