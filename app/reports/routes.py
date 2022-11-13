from flask import render_template, request
from flask_login import LoginManager, login_required, current_user

from sqlalchemy import text, func

import datetime
from dateutil import relativedelta

from app import db
from reports import reports
from reports.forms import ReportForm
from company.models import Company
from sales.models import Sales, SalesLine, SalesSchema
from purchase.models import Purchase, PurchaseLine

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


@reports.route('/reports/68/<debit_note_id>')
@login_required
def reports_68(debit_note_id):
    header_data = text("SELECT debit_note.*,company.*, suppliers.*, "
                       "DATE_FORMAT(debit_note.dn_issue_date, '%d-%m-%Y') DATEONLY ,"
                       "DATE_FORMAT(debit_note.dn_issue_date, '%H:%i:%s') TIMEONLY "
                       "FROM `debit_note`,company, suppliers "
                       "WHERE debit_note.`id`= :debit_note_id LIMIT 1 ")
    header = db.session.execute(header_data, {'debit_note_id': debit_note_id})

    t1 = text(
        "SELECT dbi.*, db.debit_note_no, db.note, db.vehicle_info, "
        "DATE_FORMAT(db.dn_issue_date, '%d-%m-%Y') DATEONLY, "
        "DATE_FORMAT(db.dn_issue_date, '%H:%i:%s') TIMEONLY, "
        "s.supplier_name,  s.supplier_bin, s.supplier_address, "
        "p.vendor_invoice, p.challan_date "
        "FROM debit_note_line AS dbi, debit_note AS db, suppliers AS s, purchase AS p "
        "WHERE dbi.debit_note_id = db.id AND db.supplier_id = s.id AND db.purchase_id = p.id "
        "AND db.debit_note_type = 3 AND db.id = :debit_note_id")

    t_1 = db.session.execute(t1, {'debit_note_id': debit_note_id})

    return render_template('reports/reports_68.html', header=header, t_1=t_1)


@reports.route('/reports/91/')
@login_required
def reports_91():
    form = ReportForm(request.form)
    return render_template('reports/index_91.html', form=form)


@reports.route('/reports/91/', methods=['GET', 'POST'])
@login_required
def reports_91_by_date():
    date = request.form['date']
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()

    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    company_data = Company.query.all()
    t1 = text(
        "SELECT SUM(purchase_line.`vatable_value`) AS vatable_value, SUM(purchase_line.`vat_amount`) AS vat_amount "
        "FROM purchase "
        "JOIN purchase_line ON purchase.id = purchase_line.purchase_id "
        "WHERE purchase_line.vat_type = 1 "
        "AND purchase_line.purchase_date between :start_date AND :end_date")
    t_1 = db.session.execute(t1, {'start_date': start_date, 'end_date': end_date})

    t5 = text(
        "SELECT SUM(purchase_line.`vatable_value`) AS vatable_value, SUM(purchase_line.`vat_amount`) AS vat_amount "
        "FROM purchase "
        "JOIN purchase_line ON purchase.id = purchase_line.purchase_id "
        "WHERE purchase_line.vat_type = 5 "
        "AND purchase_line.purchase_date between :start_date AND :end_date ")
    t_5 = db.session.execute(t5, {'start_date': start_date, 'end_date': end_date})

    t2 = text(
        "SELECT SUM(purchase_line.`vatable_value`) AS vatable_value "
        "FROM purchase "
        "JOIN purchase_line ON purchase.id = purchase_line.purchase_id "
        "WHERE purchase_line.vat_type = 2 "
        "AND purchase_line.purchase_date between :start_date AND :end_date ")
    t_2 = db.session.execute(t2, {'start_date': start_date, 'end_date': end_date})

    t3 = text(
        "SELECT SUM(purchase_line.`vatable_value`) AS vatable_value "
        "FROM purchase "
        "JOIN purchase_line ON purchase.id = purchase_line.purchase_id "
        "WHERE purchase_line.vat_type = 3 "
        "AND purchase_line.purchase_date between :start_date AND :end_date ")
    t_3 = db.session.execute(t3, {'start_date': start_date, 'end_date': end_date})

    t4 = text(
        "SELECT SUM(purchase_line.`vatable_value`) AS vatable_value, SUM(purchase_line.`vat_amount`) AS vat_amount "
        "FROM purchase "
        "JOIN purchase_line ON purchase.id = purchase_line.purchase_id "
        "WHERE purchase_line.vat_type = 4 "
        "AND purchase_line.purchase_date between :start_date AND :end_date ")
    t_4 = db.session.execute(t4, {'start_date': start_date, 'end_date': end_date})

    s1 = text(
        "SELECT SUM(sales_line.`vatable_value`) AS vatable_value, SUM(sales_line.`vat_amount`) AS vat_amount, "
        "SUM(sales_line.`sd_amount`) AS sd_amount "
        "FROM sales "
        "JOIN sales_line ON sales.id = sales_line.sales_id "
        "WHERE sales_line.vat_type = 1 "
        "AND sales_line.sales_date between :start_date AND :end_date ")
    s_1 = db.session.execute(s1, {'start_date': start_date, 'end_date': end_date})

    s2 = text(
        "SELECT SUM(sales_line.`vatable_value`) AS vatable_value, SUM(sales_line.`vat_amount`) AS vat_amount, "
        "SUM(sales_line.`sd_amount`) AS sd_amount "
        "FROM sales "
        "JOIN sales_line ON sales.id = sales_line.sales_id "
        "WHERE sales_line.vat_type = 2 "
        "AND sales_line.sales_date between :start_date AND :end_date ")
    s_2 = db.session.execute(s2, {'start_date': start_date, 'end_date': end_date})

    s3 = text(
        "SELECT SUM(sales_line.`vatable_value`) AS vatable_value, SUM(sales_line.`vat_amount`) AS vat_amount, "
        "SUM(sales_line.`sd_amount`) AS sd_amount "
        "FROM sales "
        "JOIN sales_line ON sales.id = sales_line.sales_id "
        "WHERE sales_line.vat_type = 3 "
        "AND sales_line.sales_date between :start_date AND :end_date ")
    s_3 = db.session.execute(s3, {'start_date': start_date, 'end_date': end_date})

    s4 = text(
        "SELECT SUM(sales_line.`vatable_value`) AS vatable_value, SUM(sales_line.`vat_amount`) AS vat_amount, "
        "SUM(sales_line.`sd_amount`) AS sd_amount "
        "FROM sales "
        "JOIN sales_line ON sales.id = sales_line.sales_id "
        "WHERE sales_line.vat_type = 4 "
        "AND sales_line.sales_date between :start_date AND :end_date ")
    s_4 = db.session.execute(s4, {'start_date': start_date, 'end_date': end_date})

    s5 = text(
        "SELECT SUM(sales_line.`vatable_value`) AS vatable_value, SUM(sales_line.`vat_amount`) AS vat_amount, "
        "SUM(sales_line.`sd_amount`) AS sd_amount "
        "FROM sales "
        "JOIN sales_line ON sales.id = sales_line.sales_id "
        "WHERE sales_line.vat_type = 5 "
        "AND sales_line.sales_date between :start_date AND :end_date ")
    s_5 = db.session.execute(s5, {'start_date': start_date, 'end_date': end_date})

    ivds = text(
        "SELECT SUM(`vds_amount`) AS vds_amount FROM `issue_vds_line` "
        "WHERE issue_vds_line.entry_date between :start_date AND :end_date ")
    i_vds = db.session.execute(ivds, {'start_date': start_date, 'end_date': end_date})

    rvds = text(
        "SELECT SUM(`vds_amount`) AS vds_amount FROM `receive_vds_line` "
        "WHERE receive_vds_line.entry_date between :start_date AND :end_date ")
    r_vds = db.session.execute(rvds, {'start_date': start_date, 'end_date': end_date})

    sot = text(
        "SELECT SUM(`vatable_value`) AS t_vatable_value, "
        "SUM(`sd_amount`) AS t_sd_amount, "
        "SUM(`vat_amount`) AS t_vat_amount "
        "FROM `sales_line` "
        "JOIN sales ON sales.id = sales_line.sales_id "
        "WHERE sales.entry_date between :start_date AND :end_date ")
    s_o_t = db.session.execute(sot, {'start_date': start_date, 'end_date': end_date})

    pit = text(
        "SELECT SUM(`vatable_value`) AS t_vatable_value, "
        "SUM(`vat_amount`) AS t_vat_amount "
        "FROM `purchase_line` "
        "JOIN purchase ON purchase.id = purchase_line.purchase_id "
        "WHERE purchase.entry_date between :start_date AND :end_date ")
    p_i_t = db.session.execute(pit, {'start_date': start_date, 'end_date': end_date})

    ntc = text(
        "SELECT (SELECT SUM(sales_line.`vat_amount`) FROM sales_line WHERE sales_line.sales_date between :start_date AND :end_date) AS C9, "
        "(SELECT SUM(purchase_line.`vat_amount`) FROM purchase_line WHERE purchase_line.purchase_date between :start_date AND :end_date) AS B23, "
        "(SELECT SUM(issue_vds_line.vds_amount) FROM issue_vds_line WHERE issue_vds_line.entry_date between :start_date AND :end_date) AS A28 ,"
        "(SELECT SUM(receive_vds_line.vds_amount) FROM receive_vds_line WHERE receive_vds_line.entry_date between :start_date AND :end_date) AS A33 "
        "FROM `purchase_line`, sales_line, issue_vds_line, receive_vds_line LIMIT 1"
    )
    n_t_c = db.session.execute(ntc, {'start_date': start_date, 'end_date': end_date})

    for ntc in n_t_c:
        value_34 = (ntc.C9 - ntc.B23) + (ntc.A28 - ntc.A33)
        value_35 = value_34-(52+56)

    return render_template('reports/reports_91.html', company_data=company_data,
                           t_1=t_1, t_2=t_2, t_3=t_3, t_4=t_4, t_5=t_5,
                           s_1=s_1, s_2=s_2, s_3=s_3, s_4=s_4, s_5=s_5,
                           i_vds=i_vds, r_vds=r_vds,
                           s_o_t=s_o_t, p_i_t=p_i_t, value_34=value_34, value_35=value_35
                           )
