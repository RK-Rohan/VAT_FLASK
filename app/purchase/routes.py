from flask import render_template, request, flash, redirect, url_for
from flask_login import LoginManager, login_required

from purchase import purchase
from app import db
from purchase.models import Purchase, Purchase_line
from purchase.forms import PurchaseForm, PurchaseLine

from suppliers.models import Suppliers
from items.models import Items, ItemSchema

login_manager = LoginManager()


@purchase.route('/purchase/')
@login_required
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

        data_line = [
            Purchase_line(
                item_id=request.form['items_id'],
                hs_code_id=request.form['hs_code_id'],
                purchase_id=data.id,
                qty=request.form['quantity'],
                rate=request.form['rate'],
                rate_value=request.form['rate_value'],
                sd_percent=request.form['sd_percent'],
                sd_amount=request.form['sd_bdt'],
                vatable_value=request.form['vatable_value'],
                vat_type=request.form['vat_type'],
                vat_percent=request.form['vat_percent'],
                vat_amount=request.form['vat_bdt'],
                vds=request.form['vds'],
                rebate=request.form['rebate'],
                sub_total=request.form['sub_amount'],
                grand_total=request.form['grand_total'],
                entry_date=form.entry_date.data,
                purchase_date=form.challan_date.data)
            ]
        db.session.add_all(data_line)
        db.session.commit()

    flash("Purchase Store Successfully")

    return redirect(url_for('purchase.purchase_page'))
