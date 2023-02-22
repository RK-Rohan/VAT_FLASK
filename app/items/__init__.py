from flask import Blueprint

items = Blueprint('items', __name__)

from items import routes
