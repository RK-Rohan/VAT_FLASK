import json

from flask import render_template, request, flash, redirect, url_for, jsonify
from flask_login import LoginManager, login_required

from purchase import purchase
from app import db
from purchase.models import Purchase
from purchase.forms import PurchaseForm

from suppliers.models import Suppliers
from items.models import Items, ItemSchema

login_manager = LoginManager()


@purchase.route('/purchase/')
def purchase_page():
    form = PurchaseForm(request.form)
    result = Purchase.query.all()
    # result = db.session.execute(
    #     "SELECT items.*, hs_code.hs_code, units.unit_name "
    #     "FROM `items` "
    #     "JOIN units ON items.unit_id = units.id "
    #     "JOIN hs_code  ON items.hs_code = hs_code.id "
    # )
    return render_template('purchase/index.html', purchase=result, form=form)


@purchase.route('/purchase/create/', methods=['GET', 'POST'])
def purchase_create():
    form = PurchaseForm(request.form)
    form.supplier_id.choices = [(suppliers.id, suppliers.supplier_name) for suppliers in Suppliers.query.all()]
    if request.method == "GET":
        items = Items.query.all()
        result = db.session.execute(
            "SELECT items.item_name "
            "FROM `items` "
        )
    return render_template('purchase/create.html', form=form, items=result)


@purchase.route('/purchase/store/', methods=['GET', 'POST'])
def purchase_store():
    form = PurchaseForm(request.form)
    if 'purchase_store' in request.form:
        data = Purchase(
            supplier_id=form.supplier_id.data,
            entry_date=form.entry_date.data,
            challan_date=form.challan_date.data,
            purchase_type='3',
            vendor_invoice=form.challan_no.data,
        )
        db.session.add(data)
        db.session.commit()
    flash("Puchase Store Successfully")

    return redirect(url_for('purchase.purchase_page'))
