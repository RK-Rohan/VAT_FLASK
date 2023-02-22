from flask import Blueprint

receivable_voucher = Blueprint('receivable_voucher', __name__)

from receivable_voucher import routes
