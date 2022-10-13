from flask import Blueprint

purchase = Blueprint('purchase', __name__)

from purchase import routes
