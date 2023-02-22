from flask import render_template, request, flash, redirect, url_for, json
from flask_login import LoginManager, login_required, current_user
from datetime import date

from receive_vds import receive_vds
from app import db
from receive_vds.models import ReceiveVds, ReceiveVdsLine
from receive_vds.forms import ReceiveVdsForm

from customers.models import Customers

login_manager = LoginManager()


@receive_vds.route('/receive_vds/')
@login_required
def receive_vds_page():
    form = ReceiveVdsForm(request.form)
    result = ReceiveVds.query.all()

    return render_template('receive_vds/index.html', receive_vds=result, form=form)


@receive_vds.route('/receive_vds/create/', methods=['GET', 'POST'])
def receive_vds_create():
    form = ReceiveVdsForm(request.form)
    form.customer_id.choices = [(customers.id, customers.customer_name) for customers in Customers.query.all()]

    return render_template('receive_vds/create.html', form=form)


@receive_vds.route('/receive_vds/store/', methods=['GET', 'POST'])
def receive_vds_store():
    form = ReceiveVdsForm(request.form)
    vds_no = '1001'
    if 'vds_store' in request.form:
        query = db.session.execute("SELECT `vds_no` FROM `receive_vds` ORDER BY `id` DESC LIMIT 1")
        for result in query:
            vds_no = int(result.vds_no) + 1

        data = ReceiveVds(
            vds_no=vds_no,
            customer_id=form.customer_id.data,
            vds_type='3',
            entry_date=request.form['entry_date'],
            vds_certificate_no=form.vds_certificate_no.data,
            total_amount=form.total_amount.data,
            total_vat=form.total_vat.data,
            total_vds=form.total_vds.data,
            total_receive=form.total_receive.data,
            receive_date=form.receive_date.data,
            user_id=current_user.get_id()
        )

        db.session.add(data)
        db.session.commit()

        data_line = form.receive_vds_line.data
        print(data_line)
        line_data = json.loads(data_line)

        vds_id = {"vds_id": data.id}
        entry_date = {"entry_date": data.entry_date}
        for i in range(len(line_data)):
            line_data[i]["vds_id"] = vds_id["vds_id"]
            line_data[i]["entry_date"] = entry_date["entry_date"]

        # print(line_data)

        for row in line_data:
            print(row)
            vds_line = [ReceiveVdsLine(**row)]
            db.session.add_all(vds_line)
            db.session.commit()

    flash("VDS Receive Successfully")

    return redirect(url_for('receive_vds.receive_vds_page'))
