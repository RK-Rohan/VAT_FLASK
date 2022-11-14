from flask import render_template, request, flash, redirect, url_for, jsonify
from flask_login import LoginManager, login_required
from suppliers import suppliers
from app import db
from suppliers.models import Suppliers, SuppliersSchema
from suppliers.forms import SupplierForm
from company.models import Country

login_manager = LoginManager()


@suppliers.route('/suppliers/')
def suppliers_page():
    form = SupplierForm(request.form)
    form.country_id.choices = [(country.id, country.country_name) for country in Country.query.all()]
    result = db.session.execute(
        "SELECT suppliers.*, countries.country_name "
        "FROM `suppliers` "
        "JOIN countries "
        "ON suppliers.country_id = countries.id"
    )
    return render_template('suppliers/index.html', suppliers=result, form=form)


@suppliers.route('/suppliers/create', methods=['GET', 'POST'])
@login_required
def suppliers_create():
    form = SupplierForm(request.form)
    if 'add_supplier' in request.form:
        data = Suppliers(
            supplier_name=form.supplier_name.data,
            email_address=form.email_address.data,
            phone_number=form.phone_number.data,
            country_id=form.country_id.data,
            supplier_type=form.supplier_type.data,
            supplier_address=form.supplier_address.data,
            supplier_bin=form.supplier_bin.data,
            supplier_tin=form.supplier_tin.data
        )
        db.session.add(data)
        db.session.commit()

        flash("Supplier Inserted Successfully")
    return redirect(url_for('suppliers.suppliers_page'))


@suppliers.route('/suppliers/update', methods=['GET', 'POST'])
def suppliers_update():

    if request.method == 'POST':
        data = Suppliers.query.get(request.form.get('id'))

        data.supplier_name = request.form['supplier_name']
        data.email_address = request.form['email_address']
        data.phone_number = request.form['phone_number']
        data.country = request.form['country']
        data.supplier_type = request.form['supplier_type']
        data.supplier_address = request.form['supplier_address']
        data.supplier_bin = request.form['supplier_bin']
        data.supplier_tin = request.form['supplier_tin']

        db.session.commit()
        flash("Supplier Updated Successfully")

        return redirect(url_for('suppliers.suppliers_page'))


@suppliers.route('/api/suppliers/<id>/', methods=['GET', 'POST'])
def supplier_by_id(id):
    supplier_list = Suppliers.query.get(id)
    print(supplier_list)
    suppliers_schema = SuppliersSchema()
    output = suppliers_schema.dump(supplier_list)
    return jsonify(output)