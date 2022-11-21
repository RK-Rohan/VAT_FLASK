from flask import render_template, request
from flask_login import LoginManager, login_required, current_user
from decimal import Decimal

from sqlalchemy import text, func

import datetime
from dateutil import relativedelta

from app import db
from reports import reports
from reports.forms import ReportForm
from reports.models import OpeningBalance
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
        "s.supplier_name,  s.supplier_bin, s.supplier_address, "
        "p.vendor_invoice, p.challan_date "
        "FROM debit_note_line AS dbi, debit_note AS db, suppliers AS s, purchase AS p "
        "WHERE dbi.debit_note_id = db.id AND db.supplier_id = s.id AND db.purchase_id = p.id "
        "AND db.debit_note_type = 3 AND db.id = :debit_note_id")

    t_1 = db.session.execute(t1, {'debit_note_id': debit_note_id})

    return render_template('reports/reports_68.html', header=header, t_1=t_1)


@reports.route('/reports/67/<credit_note_id>')
@login_required
def reports_67(credit_note_id):
    header_data = text("SELECT credit_note.*,company.*, customers.*, "
                       "DATE_FORMAT(credit_note.cn_issue_date, '%d-%m-%Y') DATEONLY ,"
                       "DATE_FORMAT(credit_note.cn_issue_date, '%H:%i:%s') TIMEONLY "
                       "FROM `credit_note`,company, customers "
                       "WHERE credit_note.`id`= :credit_note_id LIMIT 1 ")
    header = db.session.execute(header_data, {'credit_note_id': credit_note_id})

    t1 = text(
        "SELECT cnl.*, cn.credit_note_no, cn.note, cn.vehicle_info, "
        "c.customer_name,  c.customer_bin, c.customer_address, "
        "s.sales_invoice, s.sale_date "
        "FROM credit_note_line AS cnl, credit_note AS cn, customers AS c, sales AS s "
        "WHERE cnl.credit_note_id = cn.id AND cn.customer_id = c.id AND cn.sales_id = s.id "
        "AND cn.credit_note_type = 3 AND cn.id = :credit_note_id")

    t_1 = db.session.execute(t1, {'credit_note_id': credit_note_id})

    return render_template('reports/reports_67.html', header=header, t_1=t_1)


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
        "SELECT SUM(purchase_line.`vatable_value`) AS vatable_value, "
        "SUM(purchase_line.vat_amount) AS vat_amount "
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

    for col_23ab in p_i_t:
        col_23a = col_23ab.t_vatable_value
        col_23b = col_23ab.t_vat_amount

    ntc = text(
        "SELECT (SELECT SUM(sales_line.`vat_amount`) FROM sales_line "
        "WHERE sales_line.sales_date between :start_date AND :end_date) AS C9, "
        "(SELECT SUM(purchase_line.`vat_amount`) FROM purchase_line "
        "WHERE purchase_line.purchase_date between :start_date AND :end_date) AS B23, "
        "(SELECT SUM(issue_vds_line.vds_amount) FROM issue_vds_line "
        "WHERE issue_vds_line.entry_date between :start_date AND :end_date) AS A24 ,"
        "(SELECT SUM(receive_vds_line.vds_amount) FROM receive_vds_line "
        "WHERE receive_vds_line.entry_date between :start_date AND :end_date) AS A29 ,"
        "(SELECT SUM(debit_note_line.return_vat) FROM debit_note_line "
        "WHERE debit_note_line.entry_date between :start_date AND :end_date) AS A26, "
        "(SELECT SUM(debit_note_line.return_sd) FROM debit_note_line "
        "WHERE debit_note_line.entry_date between :start_date AND :end_date) AS A38, "
        "(SELECT SUM(credit_note_line.return_vat) FROM credit_note_line "
        "WHERE credit_note_line.entry_date between :start_date AND :end_date) AS A31, "
        "(SELECT SUM(credit_note_line.return_sd) FROM credit_note_line "
        "WHERE credit_note_line.entry_date between :start_date AND :end_date) AS A39 "
        "FROM `purchase_line`, sales_line, issue_vds_line, receive_vds_line, debit_note_line LIMIT 1"
    )
    n_t_c = db.session.execute(ntc, {'start_date': start_date, 'end_date': end_date})

    for ntc in n_t_c:
        col_9c = Decimal(ntc.C9)
        col_b23 = Decimal(ntc.B23)
        col_a24 = Decimal(ntc.A24)
        col_a26 = Decimal(ntc.A26)
        col_a28 = col_a24 + col_a26
        col_a29 = Decimal(ntc.A29)
        col_a31 = Decimal(ntc.A31)
        col_a33 = col_a29 + col_a31
        col_34 = col_9c - col_b23 + col_a28 - col_a33
        col_38 = ntc.A38
        col_39 = ntc.A39

    # opening_balance = text(
    #     "SELECT * FROM opening_balance WHERE opening_balance.closing_date between :start_date AND :end_date"
    # )
    opening_balance = OpeningBalance.query.all()
    # o_p = db.session.execute(opening_balance, {'start_date': start_date, 'end_date': end_date})
    # for op in o_p:
    #     opening_vat = op.opening_vat
    #     opening_sd = op.opening_sd

    treasury_chalan = text(
        "SELECT * FROM treasury_chalan WHERE treasury_chalan.t_date between :start_date AND :end_date"
    )
    t_c = db.session.execute(treasury_chalan, {'start_date': start_date, 'end_date': end_date})

    for tc in t_c:
        t_amount = tc.t_amount
        t_account_code = tc.t_account_code
        t_type = tc.t_type
        if t_type == 58:
            col_58a = t_account_code
            col_58b = t_amount
        else:
            col_58a = '0'
            col_58b = '0'
        if t_type == 59:
            col_59a = t_account_code
            col_59b = t_amount
        else:
            col_59a = '0'
            col_59b = '0'
        if t_type == 60:
            col_60a = t_account_code
            col_60b = t_amount
        else:
            col_60a = '0'
            col_60b = '0'
        if t_type == 61:
            col_61a = t_account_code
            col_61b = t_amount
        else:
            col_61a = '0'
            col_61b = '0'
        if t_type == 62:
            col_62a = t_account_code
            col_62b = t_amount
        else:
            col_62a = '0'
            col_62b = '0'
        if t_type == 63:
            col_63a = t_account_code
            col_63b = t_amount
        else:
            col_63a = '0'
            col_63b = '0'
        if t_type == 64:
            col_64a = t_account_code
            col_64b = t_amount
        else:
            col_64a = '0'
            col_64b = '0'

    payable_mushak = text(
        "SELECT * FROM payable_mushak WHERE payable_mushak.pay_date between :start_date AND :end_date"
    )
    p_m = db.session.execute(payable_mushak, {'start_date': start_date, 'end_date': end_date})

    for pm in p_m:
        pay_amount = pm.pay_amount
        pay_type = pm.pay_type
        if pay_type == 41:
            col_41 = pay_amount
        else:
            col_41 = '0'
        if pay_type == 42:
            col_42 = pay_amount
        else:
            col_42 = '0'
        if pay_type == 43:
            col_43 = pay_amount
        else:
            col_43 = '0'
        if pay_type == 44:
            col_44 = pay_amount
        else:
            col_44 = '0'
        if pay_type == 45:
            col_45 = pay_amount
        else:
            col_45 = '0'
        if pay_type == 46:
            col_46 = pay_amount
        else:
            col_46 = '0'
        if pay_type == 47:
            col_47 = pay_amount
        else:
            col_47 = '0'
        if pay_type == 48:
            col_48 = pay_amount
        else:
            col_48 = '0'
        if pay_type == 49:
            col_49 = pay_amount
        else:
            col_49 = '0'

    return render_template('reports/reports_91.html', company_data=company_data, date=date,
                           start_date=start_date, end_date=end_date,
                           t_1=t_1, t_2=t_2, t_3=t_3, t_4=t_4, t_5=t_5,
                           s_1=s_1, s_2=s_2, s_3=s_3, s_4=s_4, s_5=s_5,
                           s_o_t=s_o_t, col_9c=col_9c, col_23a=col_23a, col_23b=col_23b,
                           col_a24=col_a24, col_a26=col_a26,
                           col_a28=col_a28, col_a29=col_a29, col_a31=col_a31,
                           col_a33=col_a33, col_34=col_34, col_38=col_38, col_39=col_39,
                           opening_balance=opening_balance,
                           col_41=col_41, col_42=col_42, col_43=col_43, col_44=col_44, col_45=col_45,
                           col_46=col_46, col_47=col_47, col_48=col_48, col_49=col_49,
                           col_58a=col_58a, col_58b=col_58b, col_59a=col_59a, col_59b=col_59b,
                           col_60a=col_60a, col_60b=col_60b, col_61a=col_61a, col_61b=col_61b,
                           col_62a=col_62a, col_62b=col_62b, col_63a=col_63a, col_63b=col_63b,
                           col_64a=col_64a, col_64b=col_64b
                           )


@reports.route('/reports/note4/<date>/')
@login_required
def note_4(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT sl.vatable_value, sl.sd_amount, sl.vat_amount, items.item_name, items.hs_code, hs_code.description "
        "FROM `sales_line` sl JOIN items ON items.id = sl.item_id JOIN hs_code ON hs_code.id = sl.hs_code_id "
        "WHERE sl.vat_type = '1'  AND sl.sales_date between :start_date AND :end_date "
    )
    note4 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_4.html', note4=note4)


@reports.route('/reports/note1/<date>/')
@login_required
def note_1(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT sl.vatable_value, sl.sd_amount, sl.vat_amount, items.item_name, items.hs_code, hs_code.description "
        "FROM `sales_line` sl JOIN items ON items.id = sl.item_id JOIN hs_code ON hs_code.id = sl.hs_code_id "
        "WHERE sl.vat_type = '2'  AND sl.sales_date between :start_date AND :end_date "
    )
    note1 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_1.html', note1=note1)


@reports.route('/reports/note3/<date>/')
@login_required
def note_3(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT sl.vatable_value, sl.sd_amount, sl.vat_amount, items.item_name, items.hs_code, hs_code.description "
        "FROM `sales_line` sl JOIN items ON items.id = sl.item_id JOIN hs_code ON hs_code.id = sl.hs_code_id "
        "WHERE sl.vat_type = '3'  AND sl.sales_date between :start_date AND :end_date "
    )
    note3 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_3.html', note3=note3)


@reports.route('/reports/note6/<date>/')
@login_required
def note_6(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT sl.vatable_value, sl.sd_amount, sl.qty, sl.vat_amount, items.item_name, "
        "items.hs_code, hs_code.description , units.unit_name "
        "FROM `sales_line` sl JOIN items ON items.id = sl.item_id JOIN hs_code ON hs_code.id = sl.hs_code_id "
        "JOIN units ON units.id = items.unit_id "
        "WHERE sl.vat_type = '4'  AND sl.sales_date between :start_date AND :end_date "
    )
    note6 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_6.html', note6=note6)


@reports.route('/reports/note7/<date>/')
@login_required
def note_7(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT sl.vatable_value, sl.sd_amount, sl.qty, sl.vat_amount, items.item_name, "
        "items.hs_code, hs_code.description , units.unit_name "
        "FROM `sales_line` sl JOIN items ON items.id = sl.item_id JOIN hs_code ON hs_code.id = sl.hs_code_id "
        "JOIN units ON units.id = items.unit_id "
        "WHERE sl.vat_type = '5'  AND sl.sales_date between :start_date AND :end_date "
    )
    note7 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_7.html', note7=note7)


@reports.route('/reports/note10/<date>/')
@login_required
def note_10(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT pl.vatable_value, pl.sd_amount, pl.qty, pl.vat_amount, "
        "items.item_name, items.hs_code, hs_code.description , units.unit_name "
        "FROM purchase_line pl JOIN items ON items.id = pl.item_id "
        "JOIN hs_code ON hs_code.id = pl.hs_code_id "
        "JOIN units ON units.id = items.unit_id WHERE pl.vat_type=2 "
        "AND pl.purchase_date between :start_date AND :end_date "
    )
    note10 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_10.html', note10=note10)


@reports.route('/reports/note12/<date>/')
@login_required
def note_12(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT pl.vatable_value, pl.sd_amount, pl.qty, pl.vat_amount, "
        "items.item_name, items.hs_code, hs_code.description , units.unit_name "
        "FROM purchase_line pl JOIN items ON items.id = pl.item_id "
        "JOIN hs_code ON hs_code.id = pl.hs_code_id "
        "JOIN units ON units.id = items.unit_id WHERE pl.vat_type=3 "
        "AND pl.purchase_date between :start_date AND :end_date "
    )
    note12 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_12.html', note12=note12)


@reports.route('/reports/note14/<date>/')
@login_required
def note_14(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT pl.vatable_value, pl.sd_amount, pl.qty, pl.vat_amount, "
        "items.item_name, items.hs_code, hs_code.description , units.unit_name "
        "FROM purchase_line pl JOIN items ON items.id = pl.item_id "
        "JOIN hs_code ON hs_code.id = pl.hs_code_id "
        "JOIN units ON units.id = items.unit_id WHERE pl.vat_type=1 "
        "AND pl.purchase_date between :start_date AND :end_date "
    )
    note14 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_14.html', note14=note14)


@reports.route('/reports/note16/<date>/')
@login_required
def note_16(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT pl.vatable_value, pl.sd_amount, pl.qty, pl.vat_amount, "
        "items.item_name, items.hs_code, hs_code.description , units.unit_name "
        "FROM purchase_line pl JOIN items ON items.id = pl.item_id "
        "JOIN hs_code ON hs_code.id = pl.hs_code_id "
        "JOIN units ON units.id = items.unit_id WHERE pl.vat_type=5 "
        "AND pl.purchase_date between :start_date AND :end_date "
    )
    note16 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_16.html', note16=note16)


@reports.route('/reports/note18/<date>/')
@login_required
def note_18(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT pl.vatable_value, pl.sd_amount, pl.qty, pl.vat_amount, "
        "items.item_name, items.hs_code, hs_code.description , units.unit_name "
        "FROM purchase_line pl JOIN items ON items.id = pl.item_id "
        "JOIN hs_code ON hs_code.id = pl.hs_code_id "
        "JOIN units ON units.id = items.unit_id WHERE pl.vat_type=4 "
        "AND pl.purchase_date between :start_date AND :end_date "
    )
    note18 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_18.html', note18=note18)


@reports.route('/reports/note24/<date>/')
@login_required
def note_24(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT svi.*,sv.vds_no,s.supplier_name,s.supplier_bin,s.supplier_address "
        "FROM issue_vds_line AS svi,issue_vds AS sv,suppliers AS s "
        "WHERE svi.vds_id=sv.id AND svi.supplier_id=s.id "
        "AND svi.entry_date between :start_date AND :end_date "
    )
    note24 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_24.html', note24=note24)


@reports.route('/reports/note26/<date>/')
@login_required
def note_26(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT items.item_name, dnl.* FROM debit_note_line AS dnl "
        "JOIN items ON items.id = dnl.item_id "
        "AND dnl.entry_date between :start_date AND :end_date "
    )
    note26 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_26.html', note26=note26)


@reports.route('/reports/note29/<date>/')
@login_required
def note_29(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT rvi.*,rv.vds_no,c.customer_name,c.customer_bin,c.customer_address "
        "FROM receive_vds_line AS rvi,receive_vds AS rv,customers AS c "
        "WHERE rvi.vds_id=rv.id AND rvi.customer_id=c.id "
        "AND rvi.entry_date between :start_date AND :end_date "
    )
    note29 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_29.html', note29=note29)


@reports.route('/reports/note31/<date>/')
@login_required
def note_31(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT cdi.*, cd.credit_note_no, cd.total_vat, cd.total_sd, "
        "c.customer_name, c.customer_bin, c.customer_address "
        "FROM credit_note_line AS cdi, credit_note AS cd, customers AS c "
        "WHERE cdi.credit_note_id=cd.id AND cd.customer_id=c.id "
        "AND cdi.entry_date between :start_date AND :end_date "
    )
    note31 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_31.html', note31=note31)


@reports.route('/reports/note38/<date>/')
@login_required
def note_38(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT svi.*,sv.debit_note_no,sv.total_vat,sv.total_sd, "
        "s.supplier_name,s.supplier_bin,s.supplier_address "
        "FROM debit_note_line AS svi,debit_note AS sv,suppliers AS s "
        "WHERE svi.debit_note_id=sv.id AND sv.supplier_id=s.id "
        "AND svi.entry_date between :start_date AND :end_date "
    )
    note38 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_38.html', note38=note38)


@reports.route('/reports/note39/<date>/')
@login_required
def note_39(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT cdi.*,cd.credit_note_no,cd.total_vat,cd.total_sd, "
        "c.customer_name,c.customer_bin,c.customer_address "
        "FROM credit_note_line AS cdi,credit_note AS cd,customers AS c "
        "WHERE cdi.credit_note_id=cd.id AND cd.customer_id=c.id "
        "AND cdi.entry_date between :start_date AND :end_date "
    )
    note39 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_39.html', note39=note39)


@reports.route('/reports/note58/<date>/')
@login_required
def note_58(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT tc.* FROM treasury_chalan AS tc WHERE tc.t_type=58 "
        "AND tc.execute_date between :start_date AND :end_date "
    )
    note58 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_58.html', note58=note58)


@reports.route('/reports/note59/<date>/')
@login_required
def note_59(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT tc.* FROM treasury_chalan AS tc WHERE tc.t_type=59 "
        "AND tc.execute_date between :start_date AND :end_date "
    )
    note59 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_59.html', note59=note59)


@reports.route('/reports/note60/<date>/')
@login_required
def note_60(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT tc.* FROM treasury_chalan AS tc WHERE tc.t_type=60 "
        "AND tc.execute_date between :start_date AND :end_date "
    )
    note60 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_60.html', note60=note60)


@reports.route('/reports/note61/<date>/')
@login_required
def note_61(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT tc.* FROM treasury_chalan AS tc WHERE tc.t_type=61 "
        "AND tc.execute_date between :start_date AND :end_date "
    )
    note61 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_61.html', note61=note61)


@reports.route('/reports/note62/<date>/')
@login_required
def note_62(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT tc.* FROM treasury_chalan AS tc WHERE tc.t_type=62 "
        "AND tc.execute_date between :start_date AND :end_date "
    )
    note62 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_62.html', note62=note62)


@reports.route('/reports/note63/<date>/')
@login_required
def note_63(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT tc.* FROM treasury_chalan AS tc WHERE tc.t_type=63 "
        "AND tc.execute_date between :start_date AND :end_date "
    )
    note63 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_63.html', note63=note63)


@reports.route('/reports/note64/<date>/')
@login_required
def note_64(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_date = datetime.date(date.year, date.month, 1)
    end_date = start_date + relativedelta.relativedelta(months=1, day=1, days=-1)

    query = text(
        "SELECT tc.* FROM treasury_chalan AS tc WHERE tc.t_type=64 "
        "AND tc.execute_date between :start_date AND :end_date "
    )
    note64 = db.session.execute(query, {'start_date': start_date, 'end_date': end_date})

    return render_template('reports/note/note_64.html', note64=note64)

