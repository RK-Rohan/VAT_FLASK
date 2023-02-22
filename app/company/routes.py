from flask import render_template, request, redirect, url_for
from company import company
from flask_login import LoginManager, login_required


from app import db, csrf
from company.models import Company, Country

from company.forms import CompanyForm

login_manager = LoginManager()


@company.route('/company/master', methods=['GET', 'POST'])
@login_required
def company_post():
    form = CompanyForm(request.form)
    form.country.choices = [(country.id, country.country_name) for country in Country.query.all()]
    if 'company' in request.form:
        data = Company(
            company_name=form.company_name.data,
            short_name=form.short_name.data,
            email_address=form.email_address.data,
            phone_number=form.phone_number.data,
            country=form.country.data,
            address=form.address.data,
            bank_name=form.bank_name.data,
            ac_number=form.ac_number.data,
            branch=form.branch.data,
            business_nature=form.business_nature.data,
            business_economics=form.business_economics.data,
            vat_type=form.vat_type.data,
            bin_number=form.bin_number.data,
            tin_number=form.tin_number.data,
            currency=form.currency.data,
            person_name=form.person_name.data,
            designation=form.designation.data,
            person_phone_number=form.person_phone_number.data,
            nid=form.nid.data,
            person_email=form.person_email.data
        )
        db.session.add(data)
        db.session.commit()
    return render_template('company/index.html', success=True, form=form)


@company.route('/company/edit/', methods=['POST', 'GET'])
@login_required
def company_update():
    company_data = Company.query.filter(Company.id == 1).first()
    if request.method == 'POST':
        form = CompanyForm(formdata=request.form, obj=company_data)
        form.populate_obj(company_data)
        db.session.commit()
        return redirect(url_for('company.company_update', id=company_data.id))
    form = CompanyForm(obj=company_data)
    form.country.choices = [(country.id, country.country_name) for country in Country.query.all()]
    return render_template('company/edit.html', company_data=company, form=form)

