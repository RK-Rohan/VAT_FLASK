from flask import render_template, request, flash, redirect, url_for, json, jsonify
from flask_login import LoginManager, login_required, current_user

from app import db
from sales import sales
from sales.models import Sales, SalesLine, SalesSchema
from sales.forms import SalesForm

from customers.models import Customers
from items.models import Items

login_manager = LoginManager()


@sales.route('/sales/')
@login_required
def sales_page():
    form = SalesForm(request.form)
    result = Sales.query.all()
    # result = db.session.execute(
    #     "SELECT items.*, hs_code.hs_code, units.unit_name "
    #     "FROM `items` "
    #     "JOIN units ON items.unit_id = units.id "
    #     "JOIN hs_code  ON items.hs_code = hs_code.id "
    # )
    return render_template('sales/index.html', sales=result, form=form)


@sales.route('/sales/create/', methods=['GET', 'POST'])
def sales_create():
    form = SalesForm(request.form)
    form.customer_id.choices = [(customers.id, customers.customer_name) for customers in Customers.query.all()]

    if request.method == "GET":
        result = Items.query.all()
        # result = db.session.execute(
        #     "SELECT items.item_name "
        #     "FROM `items` "
        # )
    return render_template('sales/create.html', form=form, items=result)

    flash("Sales Store Successfully")

    return redirect(url_for('sales.sales_page'))


@sales.route('/sales/store/', methods=['GET', 'POST'])
def sales_store():
    form = SalesForm(request.form)
    if 'sales_store' in request.form:

        data = Sales(
            customer_id=form.customer_id.data,
            sale_date=form.sale_date.data,
            vehicle_info=form.vehicle_info.data,
            destination=form.destination.data,
            sales_type='3',
            # total_discount=form.grand_total.data,
            total_sd=form.total_sd.data,
            total_vat=form.total_vat.data,
            grand_total=form.grand_total.data,
            user_id=current_user.get_id()
        )
        db.session.add(data)
        db.session.commit()

        data_line = form.sales_line.data
        line_data = json.loads(data_line)

        sales_id = {"sales_id": data.id}
        sales_date = {"sales_date": request.form['sale_date']}
        # entry_date = {"entry_date": request.form['entry_date']}
        for i in range(len(line_data)):
            line_data[i]["sales_id"] = sales_id["sales_id"]
            line_data[i]["sales_date"] = sales_date["sales_date"]
            # line_data[i]["entry_date"] = entry_date["entry_date"]

        # print(line_data)

        for row in line_data:
            print(row)
            sales_line = [SalesLine(**row)]
            db.session.add_all(sales_line)
            db.session.commit()

    flash("Sales Store Successfully")

    return redirect(url_for('sales.sales_page'))


@sales.route('/api/sales/customers/<customer_id>/', methods=['GET', 'POST'])
def sales_by_customer_id(customer_id):
    sales_list = Sales.query.join(SalesLine, Sales.id == SalesLine.sales_id)\
        .add_columns\
        (
            Sales.id,
            Sales.customer_id,
            Sales.sales_invoice,
            Sales.sale_date,
            Sales.total_sd,
            Sales.total_vat,
            Sales.grand_total,
            Sales.entry_date,
            Sales.user_id
        ).filter(Sales.customer_id == customer_id)
    print(sales_list)
    sales_schema = SalesSchema()
    output = sales_schema.dump(sales_list, many=True)
    return jsonify(output)\



@sales.route('/api/sales/<id>/', methods=['GET', 'POST'])
def sales_by_id(id):
    sales_list = Sales.query.get(id)
    print(sales_list)
    sales_schema = SalesSchema()
    output = sales_schema.dump(sales_list)
    return jsonify(output)


# @purchase.route('/api/purchase/', methods=['GET', 'POST'])
# def purchase_all():
#     purchase_list = Purchase.query.all()
#     print(purchase_list)
#     purchase_schema = PurchaseSchema()
#     output = purchase_schema.dump(purchase_list, many=True)
#     return jsonify(output)\
#
#
#