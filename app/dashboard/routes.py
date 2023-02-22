from flask import render_template
from dashboard import dashboard
from flask_login import LoginManager, login_required

login_manager = LoginManager()


@dashboard.route('/home')
@login_required
def home_page():
    return render_template('dashboard/index.html')
