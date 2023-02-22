from flask import render_template, request, flash, redirect, url_for, json
from flask_login import LoginManager, login_required, current_user
from datetime import date, datetime

from debit_note import debit_note
from app import db
from debit_note.models import DebitNote, DebitNoteLine
from debit_note.forms import DebitNoteForm

from suppliers.models import Suppliers

login_manager = LoginManager()


@debit_note.route('/debit_note/')
@login_required
def debit_note_page():
    form = DebitNoteForm(request.form)
    result = DebitNote.query.all()

    return render_template('debit_note/index.html', debit_note=result, form=form)


@debit_note.route('/debit_note/create/', methods=['GET', 'POST'])
def debit_note_create():
    form = DebitNoteForm(request.form)
    form.supplier_id.choices = [(suppliers.id, suppliers.supplier_name) for suppliers in Suppliers.query.all()]

    return render_template('debit_note/create.html', form=form)


@debit_note.route('/debit_note/store/', methods=['GET', 'POST'])
def debit_note_store():
    form = DebitNoteForm(request.form)
    debit_note_no = '1001'
    if 'debit_note_store' in request.form:
        query = db.session.execute("SELECT `debit_note_no` FROM `debit_note` ORDER BY `id` DESC LIMIT 1")
        for result in query:
            debit_note_no = int(result.debit_note_no) + 1

        data = DebitNote(
            debit_note_no=debit_note_no,
            purchase_id=form.purchase_id.data,
            supplier_id=form.supplier_id.data,
            vehicle_info=form.vehicle_info.data,
            debit_note_type='3',
            dn_issue_date=request.form['dn_issue_date'],
            total_amount=request.form['total_amount'],
            total_vat=request.form['total_vat'],
            total_sd=request.form['total_sd'],
            created_at=datetime.now(),
            user_id=current_user.get_id()
        )

        db.session.add(data)
        db.session.commit()

        data_line = form.debit_note_line.data
        print(data_line)
        line_data = json.loads(data_line)

        debit_note_id = {"debit_note_id": data.id}
        entry_date = {"entry_date": data.dn_issue_date}
        for i in range(len(line_data)):
            line_data[i]["debit_note_id"] = debit_note_id["debit_note_id"]
            line_data[i]["entry_date"] = entry_date["entry_date"]

        # print(line_data)

        for row in line_data:
            print(row)
            debit_note_line = [DebitNoteLine(**row)]
            db.session.add_all(debit_note_line)
            db.session.commit()

    flash("Debit Note Issue Successfully")

    return redirect(url_for('debit_note.debit_note_page'))
