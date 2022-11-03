from flask import render_template
from flask_login import LoginManager, login_required, current_user

from sqlalchemy import text


from app import db
from reports import reports
from company.models import Company
from sales.models import Sales, SalesLine, SalesSchema
from purchase.models import Purchase, Purchase_line

from customers.models import Customers
from suppliers.models import Suppliers
from items.models import Items
from units.models import Units

from issue_vds.models import IssueVds, IssueVdsLine

login_manager = LoginManager()


@reports.route('/reports/63/<sale_id>')
@login_required
def reports_63(sale_id):
    company_data = Company.query.all()

    t = text("SELECT sales.id, DATE_FORMAT(sales.`entry_date`, '%d-%m-%Y')DATEONLY, "
             "DATE_FORMAT(sales.`entry_date`, '%H:%i:%s') TIMEONLY, "
             "customers.customer_name, customers.customer_bin, sales.sales_invoice, sales.destination "
             "FROM `sales` "
             "JOIN customers ON customers.id = sales.customer_id "
             "WHERE sales.id = :id")

    customers = db.session.execute(t, {'id': sale_id})

    sales_data = Sales.query.join(Customers, Customers.id == Sales.customer_id) \
        .join(SalesLine, Sales.id == SalesLine.sales_id) \
        .join(Items, Items.id == SalesLine.item_id) \
        .join(Units, Units.id == Items.unit_id) \
        .add_columns \
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
        ) \
        .filter(Sales.id == sale_id)

    totals = Sales.query.filter(Sales.id == sale_id)

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

    return render_template('reports/reports_63.html', company_data=company_data, customers=customers,
                           sales_data=sales_data, totals=totals)


@reports.route('/reports/66/<vds_id>')
@login_required
def reports_66(vds_id):
    company_data = Company.query.all()
    vds_table = IssueVds.query.filter(IssueVds.id == vds_id)

    vds_data = IssueVds.query.join(Suppliers, Suppliers.id == IssueVds.supplier_id) \
        .join(IssueVdsLine, IssueVds.id == IssueVdsLine.vds_id) \
        .join(Purchase, Purchase.p_invoice_no == IssueVdsLine.invoice_no) \
        .add_columns \
        (
            IssueVds.id,
            Suppliers.supplier_name,
            Suppliers.supplier_bin,
            IssueVdsLine.invoice_no,
            IssueVdsLine.inv_date,
            IssueVdsLine.inv_amount,
            IssueVdsLine.vat_amount,
            IssueVdsLine.vds_amount,
        ) \
        .filter(Sales.id == vds_id)

    return render_template('reports/reports_66.html', company_data=company_data, vds_table=vds_table, vds_data=vds_data)


@reports.route('/reports/91/')
@login_required
def reports_91():
    company_data = Company.query.all()
    # vds_table = IssueVds.query.filter(IssueVds.id == vds_id)

    return render_template('reports/reports_91.html', company_data=company_data)
