from flask import render_template, request, flash, redirect, url_for, json
from flask_login import LoginManager, login_required, current_user

from app import db
from sales import sales

login_manager = LoginManager()


@sales.route('/sales/')
@login_required
def sales_page():
    # form = PurchaseForm(request.form)
    # result = Purchase.query.all()
    # result = db.session.execute(
    #     "SELECT items.*, hs_code.hs_code, units.unit_name "
    #     "FROM `items` "
    #     "JOIN units ON items.unit_id = units.id "
    #     "JOIN hs_code  ON items.hs_code = hs_code.id "
    # )
    # return render_template('purchase/index.html', purchase=result, form=form)

    return "sales Page"


# @purchase.route('/purchase/create/', methods=['GET', 'POST'])
# def purchase_create():
#     form = PurchaseForm(request.form)
#     form.supplier_id.choices = [(suppliers.id, suppliers.supplier_name) for suppliers in Suppliers.query.all()]
#     if request.method == "GET":
#         items = Items.query.all()
#         result = db.session.execute(
#             "SELECT items.item_name "
#             "FROM `items` "
#         )
#     return render_template('purchase/create.html', form=form, items=result)
#
#     flash("Purchase Store Successfully")
#
#     return redirect(url_for('purchase.purchase_page'))
