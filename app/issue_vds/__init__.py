from flask import Blueprint

issue_vds = Blueprint('issue_vds', __name__)

from issue_vds import routes
