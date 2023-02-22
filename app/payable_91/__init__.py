from flask import Blueprint

payable_91 = Blueprint('payable_91', __name__)

from payable_91 import routes
