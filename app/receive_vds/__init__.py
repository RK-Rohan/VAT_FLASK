from flask import Blueprint

receive_vds = Blueprint('receive_vds', __name__)

from receive_vds import routes
