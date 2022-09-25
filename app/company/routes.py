from flask import render_template, request, redirect, url_for
from company import company
from flask_login import LoginManager, login_required

from company.forms import CompanyForm

login_manager = LoginManager()


@company.route('/company', methods=['GET', 'POST'])
def company_post():
    company_form = CompanyForm(request.form)

    return render_template('company/index.html', success=False, form=company_form)

