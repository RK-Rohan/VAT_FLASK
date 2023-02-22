from flask import Blueprint

credit_note = Blueprint('credit_note', __name__)

from credit_note import routes
