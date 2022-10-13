from flask import render_template, request, flash, redirect, url_for
from flask_login import LoginManager, login_required

from purchase import purchase
from app import db
from purchase.models import Purchase
from purchase.forms import PurchaseForm

from suppliers.models import Suppliers

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
        items = ["C++", "Python", "PHP", "Java", "C", "Ruby"]
    return render_template('purchase/create.html', form=form, items=items)
#
#
# @items.route('/items/store/', methods=['GET', 'POST'])
# def items_store():
#     form = ItemsForm(request.form)
#     # hs_code_id = form.hs_code.data
#     # hs_code = db.session.execute("SELECT hs_code FROM hs_code WHERE id = %s", [hs_code_id])
#
#     if 'item_create' in request.form:
#         data = Items(
#             item_name=form.item_name.data,
#             unit_id=form.unit_id.data,
#             hs_code=form.hs_code.data,
#             hs_code_id=form.hs_code.data,
#             item_type=form.item_type.data,
#         )
#         db.session.add(data)
#         db.session.commit()
#     flash("Item Inserted Successfully")
#
#     return redirect(url_for('items.items_page'))

