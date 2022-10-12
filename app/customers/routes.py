from flask import render_template, request, flash, redirect, url_for
from flask_login import LoginManager, login_required

from customers import customers
from app import db
from customers.models import Customers
from customers.forms import CustomersForm
from company.models import Country

login_manager = LoginManager()


@customers.route('/customers/')
def customers_page():
    form = CustomersForm(request.form)
    form.country_id.choices = [(country.id, country.country_name) for country in Country.query.all()]
    form.shipping_country.choices = [(country.id, country.country_name) for country in Country.query.all()]
    all_data = Customers.query.all()
    result = db.session.execute(
        "SELECT customers.*, countries.country_name "
        "FROM `customers` "
        "JOIN countries "
        "ON customers.country_id = countries.id"
    )
    return render_template('customers/index.html', customers=result, form=form)


@customers.route('/customers/create', methods=['GET', 'POST'])
@login_required
def customers_create():
    form = CustomersForm(request.form)
    if 'add_customer' in request.form:
        data = Customers(
            customer_name=form.customer_name.data,
            email_address=form.email_address.data,
            phone_number=form.phone_number.data,
            country_id=form.country_id.data,
            customer_type=form.customer_type.data,
            customer_address=form.customer_address.data,
            shipping_address=form.shipping_address.data,
            shipping_country=form.shipping_country.data,
            customer_bin=form.customer_bin.data,
            customer_tin=form.customer_tin.data
        )
        db.session.add(data)
        db.session.commit()
    flash("Customers Inserted Successfully")
    return redirect(url_for('customers.customers_page'))


@customers.route('/customers/update', methods=['GET', 'POST'])
def customers_update():

    if request.method == 'POST':
        data = Customers.query.get(request.form.get('id'))

        data.customer_name = request.form['customer_name']
        data.email_address = request.form['email_address']
        data.phone_number = request.form['phone_number']
        data.country_id = request.form['country_id']
        data.customer_type = request.form['customer_type']
        data.customer_address = request.form['customer_address']
        data.shipping_address = request.form['shipping_address']
        data.shipping_country = request.form['shipping_country']
        data.customer_bin = request.form['customer_bin']
        data.customer_tin = request.form['customer_tin']

        db.session.commit()
        flash("Customers Updated Successfully")

        return redirect(url_for('customers.customers_page'))
