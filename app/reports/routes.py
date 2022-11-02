from flask import render_template, request, flash, redirect, url_for, json, jsonify
from flask_login import LoginManager, login_required, current_user

import re

from datetime import date, datetime

from app import db
from reports import reports
from company.models import Company
from sales.models import Sales, SalesLine, SalesSchema
from sales.forms import SalesForm

from customers.models import Customers
from items.models import Items
from units.models import Units

login_manager = LoginManager()


@reports.route('/reports/63/<sale_id>')
@login_required
def reports_63(sale_id):
    company_data = Company.query.all()
        # SELECT sales.id, DATE_FORMAT(sales.`entry_date`, '%d-%m-%Y') DATEONLY,
        # DATE_FORMAT(sales.`entry_date`, '%H:%i:%s') TIMEONLY,
        # customers.customer_name, customers.customer_bin, sales.sales_invoice, sales.destination
        # FROM `sales`
        # JOIN customers ON customers.id = sales.customer_id
        # WHERE sales.id IN %(sale_id)
        # customers = db.session.execute(sql, param)

    customers = Sales.query.join(Customers, Customers.id == Sales.customer_id)\
        .add_columns\
        (
            Sales.id,
            Sales.entry_date,
            Sales.sales_invoice,
            Sales.destination,
            Customers.customer_name,
            Customers.customer_bin,
        ).filter(Sales.id == sale_id)

    sales_data = Sales.query.join(Customers, Customers.id == Sales.customer_id)\
        .join(SalesLine, Sales.id == SalesLine.sales_id) \
        .join(Items, Items.id == SalesLine.item_id) \
        .join(Units, Units.id == Items.unit_id) \
        .add_columns\
        (
            Sales.id,
            Items.item_name,
            Units.unit_name,
            SalesLine.qty,
            SalesLine.rate,
            SalesLine.rate_value,
            SalesLine.sd_amount,
            SalesLine.vat_percent,
            SalesLine.vat_amount,
            SalesLine.vat_amount,
            SalesLine.sub_total
        ).filter(Sales.id == sale_id)

    footer = Sales.query.filter(Sales.id == sale_id)

    print(sales_data)

    # footer = db.session.execute(
    #     "SELECT sales.total_sd, sales.total_vat, sales.grand_total "
    #     "FROM `sales` "
    #     "WHERE sales.id IN %(sale_id)s"
    # )

    # sales_data = db.session.execute(
    #     "SELECT sales.id, items.item_name, units.unit_name, "
    #     "customers.customer_name, customers.customer_bin, sales.destination, "
    #     "sales.sales_invoice, sales_line.item_id, sales_line.hs_code_id, "
    #     "sales_line.qty, sales_line.rate, sales_line.rate_value, sales_line.sd_amount, "
    #     "sales_line.vat_percent, sales_line.vat_amount, sales_line.vat_amount, sales_line.sub_total "
    #     "FROM `sales` "
    #     "JOIN customers ON customers.id = sales.customer_id "
    #     "JOIN sales_line ON sales.id = sales_line.sales_id "
    #     "JOIN items ON items.id = sales_line.item_id "
    #     "JOIN units ON units.id = items.unit_id "
    #     "WHERE sales.id IN %(sale_id)s"
    # )

    return render_template('reports/reports_63.html', company_data=company_data, customers=customers, sales_data=sales_data, footer=footer)


# @sales.route('/sales/create/', methods=['GET', 'POST'])
# def sales_create():
#     form = SalesForm(request.form)
#     form.customer_id.choices = [(customers.id, customers.customer_name) for customers in Customers.query.all()]
#
#     if request.method == "GET":
#         result = Items.query.all()
#         # result = db.session.execute(
#         #     "SELECT items.item_name "
#         #     "FROM `items` "
#         # )
#     return render_template('sales/create.html', form=form, items=result)
#
#     flash("Sales Store Successfully")
#
#     return redirect(url_for('sales.sales_page'))


# @sales.route('/sales/store/', methods=['GET', 'POST'])
# def sales_store():
#     form = SalesForm(request.form)
#     sales_invoice = 'INV1001'
#     if 'sales_store' in request.form:
#         query = db.session.execute("SELECT `sales_invoice` FROM `sales` ORDER BY `id` DESC LIMIT 1")
#         for result in query:
#             # sales_invoice = int(result.sales_invoice) + 1
#
#             # c_date = datetime.now()
#             # date_int = c_date.strftime("%Y") + c_date.strftime("%m") + c_date.strftime("%d")
#
#             sales_invoice = result.sales_invoice
#
#             sales_invoice = re.sub(r'[0-9]+$',
#                                    lambda x: f"{str(int(x.group()) + 1).zfill(len(x.group()))}", sales_invoice)
#
#         data = Sales(
#             customer_id=form.customer_id.data,
#             sale_date=form.sale_date.data,
#             entry_date=datetime.now(),
#             sales_invoice=sales_invoice,
#             vehicle_info=form.vehicle_info.data,
#             destination=form.destination.data,
#             sales_type='3',
#             # total_discount=form.grand_total.data,
#             total_sd=form.total_sd.data,
#             total_vat=form.total_vat.data,
#             grand_total=form.grand_total.data,
#             user_id=current_user.get_id()
#         )
#         db.session.add(data)
#         db.session.commit()
#
#         data_line = form.sales_line.data
#         line_data = json.loads(data_line)
#
#         sales_id = {"sales_id": data.id}
#         sales_date = {"sales_date": request.form['sale_date']}
#         # entry_date = {"entry_date": request.form['entry_date']}
#         for i in range(len(line_data)):
#             line_data[i]["sales_id"] = sales_id["sales_id"]
#             line_data[i]["sales_date"] = sales_date["sales_date"]
#             # line_data[i]["entry_date"] = entry_date["entry_date"]
#
#         # print(line_data)
#
#         for row in line_data:
#             print(row)
#             sales_line = [SalesLine(**row)]
#             db.session.add_all(sales_line)
#             db.session.commit()
#
#     flash("Sales Store Successfully")
#
#     return redirect(url_for('sales.sales_page'))
#
#
# @sales.route('/api/sales/customers/<customer_id>/', methods=['GET', 'POST'])
# def sales_by_customer_id(customer_id):
#     sales_list = Sales.query.join(SalesLine, Sales.id == SalesLine.sales_id)\
#         .add_columns\
#         (
#             Sales.id,
#             Sales.customer_id,
#             Sales.sales_invoice,
#             Sales.sale_date,
#             Sales.total_sd,
#             Sales.total_vat,
#             Sales.grand_total,
#             Sales.entry_date,
#             Sales.user_id
#         ).filter(Sales.customer_id == customer_id)
#     print(sales_list)
#     sales_schema = SalesSchema()
#     output = sales_schema.dump(sales_list, many=True)
#     return jsonify(output)\
