from flask import Blueprint

debit_note = Blueprint('debit_note', __name__)

from debit_note import routes
