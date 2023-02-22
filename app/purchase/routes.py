from flask import render_template, request, flash, redirect, url_for, json, jsonify
from flask_login import LoginManager, login_required, current_user
from sqlalchemy import text

from purchase import purchase
from app import db
from purchase.models import Purchase, PurchaseLine, PurchaseSchema, PurchaseLineSchema
from purchase.forms import PurchaseForm

from suppliers.models import Suppliers
from items.models import Items

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
    invoice_no = '1001'
    if 'purchase_store' in request.form:
        query = db.session.execute("SELECT `p_invoice_no` FROM `purchase` ORDER BY `id` DESC LIMIT 1")
        for result in query:
            invoice_no = int(result.p_invoice_no) + 1

        data = Purchase(
            supplier_id=form.supplier_id.data,
            p_invoice_no=invoice_no,
            entry_date=form.entry_date.data,
            challan_date=form.challan_date.data,
            purchase_type='3',
            vendor_invoice=form.challan_no.data,
            grand_total=form.grand_total.data,
            total_tax=request.form['total_vat'],
            user_id=current_user.get_id()
        )

        db.session.add(data)
        db.session.commit()

        data_line = form.allpurchase.data
        line_data = json.loads(data_line)

        purchase_id = {"purchase_id": data.id}
        purchase_date = {"purchase_date": request.form['challan_date']}
        entry_date = {"entry_date": request.form['entry_date']}
        for i in range(len(line_data)):
            line_data[i]["purchase_id"] = purchase_id["purchase_id"]
            line_data[i]["purchase_date"] = purchase_date["purchase_date"]
            line_data[i]["entry_date"] = entry_date["entry_date"]

        # print(line_data)

        for row in line_data:
            print(row)
            purchase_line = [PurchaseLine(**row)]
            db.session.add_all(purchase_line)
            db.session.commit()

    flash("Purchase Store Successfully")

    return redirect(url_for('purchase.purchase_page'))


@purchase.route('/api/purchase/supplier/<supplier_id>/', methods=['GET', 'POST'])
def purchase_by_supplier_id(supplier_id):
    purchase_list = Purchase.query.join(PurchaseLine, Purchase.id == PurchaseLine.purchase_id)\
        .add_columns\
        (
            Purchase.id,
            Purchase.supplier_id,
            Purchase.p_invoice_no,
            Purchase.vendor_invoice,
            Purchase.challan_date,
            Purchase.total_vds,
            Purchase.total_tax,
            Purchase.grand_total,
            Purchase.entry_date,
            Purchase.user_id
        ).filter(Purchase.supplier_id == supplier_id)
    print(purchase_list)
    purchase_schema = PurchaseSchema()
    output = purchase_schema.dump(purchase_list, many=True)
    return jsonify(output)\



@purchase.route('/api/purchase/', methods=['GET', 'POST'])
def purchase_all():
    purchase_list = Purchase.query.all()
    print(purchase_list)
    purchase_schema = PurchaseSchema()
    output = purchase_schema.dump(purchase_list, many=True)
    return jsonify(output)\



@purchase.route('/api/purchase/<id>/', methods=['GET', 'POST'])
def purchase_by_id(id):
    purchase_list = Purchase.query.get(id)
    print(purchase_list)
    purchase_schema = PurchaseSchema()
    output = purchase_schema.dump(purchase_list)
    return jsonify(output)


@purchase.route('/api/purchase_line/<purchase_id>/', methods=['GET', 'POST'])
def purchase_line_by_id(purchase_id):
    t = text(
        "SELECT p.grand_total, i.item_name, Pl.* "
        "FROM purchase_line AS Pl, purchase AS p, items AS i "
        "WHERE p.id = Pl.purchase_id AND i.id = Pl.item_id AND p.id = :purchase_id"
        )
    purchase_list = db.session.execute(t, {'purchase_id': purchase_id})
    print(purchase_list)
    purchase_schema = PurchaseLineSchema()
    output = purchase_schema.dump(purchase_list, many=True)
    return jsonify(output)

