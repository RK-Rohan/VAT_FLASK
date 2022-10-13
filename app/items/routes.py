from flask import render_template, request, flash, redirect, url_for
from flask_login import LoginManager, login_required

from items import items
from app import db
from items.models import Items, HSCode
from items.forms import ItemsForm

from units.models import Units
from units.forms import UnitsForm

login_manager = LoginManager()


@items.route('/items/')
def items_page():
    form = ItemsForm(request.form)
    # result = Items.query.all()
    result = db.session.execute(
        "SELECT items.*, hs_code.hs_code, units.unit_name "
        "FROM `items` "
        "JOIN units ON items.unit_id = units.id "
        "JOIN hs_code  ON items.hs_code = hs_code.id "
    )
    return render_template('items/index.html', items=result, form=form)


@items.route('/items/create/', methods=['GET', 'POST'])
def items_create():
    form = ItemsForm(request.form)
    unitsform = UnitsForm(request.form)
    form.unit_id.choices = [(units.id, units.unit_name) for units in Units.query.all()]
    form.hs_code.choices = [(hs_code.id, hs_code.hs_code) for hs_code in HSCode.query.all()]
    hs_code = HSCode.query.all()

    return render_template('items/create.html', form=form, hs_code=hs_code, units=unitsform)


@items.route('/items/store/', methods=['GET', 'POST'])
def items_store():
    form = ItemsForm(request.form)
    # hs_code_id = form.hs_code.data
    # hs_code = db.session.execute("SELECT hs_code FROM hs_code WHERE id = %s", [hs_code_id])

    if 'item_create' in request.form:
        data = Items(
            item_name=form.item_name.data,
            unit_id=form.unit_id.data,
            hs_code=form.hs_code.data,
            hs_code_id=form.hs_code.data,
            item_type=form.item_type.data,
        )
        db.session.add(data)
        db.session.commit()
    flash("Item Inserted Successfully")

    return redirect(url_for('items.items_page'))


# @customers.route('/customers/update', methods=['GET', 'POST'])
# def customers_update():
#
#     if request.method == 'POST':
#         data = Customers.query.get(request.form.get('id'))
#
#         data.customer_name = request.form['customer_name']
#         data.email_address = request.form['email_address']
#         data.phone_number = request.form['phone_number']
#         data.country_id = request.form['country_id']
#         data.customer_type = request.form['customer_type']
#         data.customer_address = request.form['customer_address']
#         data.shipping_address = request.form['shipping_address']
#         data.shipping_country = request.form['shipping_country']
#         data.customer_bin = request.form['customer_bin']
#         data.customer_tin = request.form['customer_tin']
#
#         db.session.commit()
#         flash("Customers Updated Successfully")
#
#         return redirect(url_for('customers.customers_page'))
