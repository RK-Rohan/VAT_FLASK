from flask import Blueprint

payable_voucher = Blueprint('payable_voucher', __name__)

from payable_voucher import routes
