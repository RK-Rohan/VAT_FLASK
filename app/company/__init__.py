from flask import Blueprint

company = Blueprint('company', __name__)

from company import routes
