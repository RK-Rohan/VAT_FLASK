from flask import render_template, request, flash, redirect, url_for, json, jsonify
from flask_login import LoginManager, login_required, current_user

from app import db
from treasury_chalan import treasury_chalan
from treasury_chalan.models import TreasuryChalan
from treasury_chalan.forms import TreasuryChalanForm

login_manager = LoginManager()


@treasury_chalan.route('/treasury_chalan/')
@login_required
def treasury_chalan_page():
    form = TreasuryChalanForm(request.form)
    result = TreasuryChalan.query.all()

    return render_template('treasury_chalan/index.html', treasury_chalan=result, form=form)


@treasury_chalan.route('/treasury_chalan/create/', methods=['GET', 'POST'])
def treasury_chalan_create():
    form = TreasuryChalanForm(request.form)

    return render_template('treasury_chalan/create.html', form=form)


# @treasury_chalan.route('/treasury_chalan/store/', methods=['GET', 'POST'])
# def treasury_chalan_store():
#     form = TreasuryChalanForm(request.form)
#
#     if 'treasury_store' in request.form:
#         data = Purchase(
#             supplier_id=form.supplier_id.data,
#             p_invoice_no=invoice_no,
#             entry_date=form.entry_date.data,
#             challan_date=form.challan_date.data,
#             purchase_type='3',
#             vendor_invoice=form.challan_no.data,
#             grand_total=form.grand_total.data,
#             total_tax=request.form['total_vat'],
#             user_id=current_user.get_id()
#         )
#
#         db.session.add(data)
#         db.session.commit()
#
#         data_line = form.allpurchase.data
#         line_data = json.loads(data_line)
#
#         purchase_id = {"purchase_id": data.id}
#         purchase_date = {"purchase_date": request.form['challan_date']}
#         entry_date = {"entry_date": request.form['entry_date']}
#         for i in range(len(line_data)):
#             line_data[i]["purchase_id"] = purchase_id["purchase_id"]
#             line_data[i]["purchase_date"] = purchase_date["purchase_date"]
#             line_data[i]["entry_date"] = entry_date["entry_date"]
#
#         # print(line_data)
#
#         for row in line_data:
#             print(row)
#             purchase_line = [PurchaseLine(**row)]
#             db.session.add_all(purchase_line)
#             db.session.commit()
#
#     flash("Purchase Store Successfully")
#
#     return redirect(url_for('purchase.purchase_page'))

