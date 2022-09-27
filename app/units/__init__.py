from flask import Blueprint

units = Blueprint('units', __name__)

from units import routes
