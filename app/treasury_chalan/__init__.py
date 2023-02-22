from flask import Blueprint

treasury_chalan = Blueprint('treasury_chalan', __name__)

from treasury_chalan import routes
