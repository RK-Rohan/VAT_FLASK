from flask import render_template, request, flash, redirect, url_for, json
from flask_login import LoginManager, login_required, current_user
from datetime import date

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


# @issue_vds.route('/issue_vds/store/', methods=['GET', 'POST'])
# def issue_vds_store():
#     form = IssueVdsForm(request.form)
#     vds_no = '1001'
#     if 'vds_store' in request.form:
#         query = db.session.execute("SELECT `vds_no` FROM `issue_vds` ORDER BY `id` DESC LIMIT 1")
#         for result in query:
#             vds_no = int(result.vds_no) + 1
#
#         data = IssueVds(
#             vds_no=vds_no,
#             supplier_id=form.supplier_id.data,
#             vds_type='3',
#             entry_date=request.form['entry_date'],
#             total_amount=form.total_amount.data,
#             total_vat=form.total_vat.data,
#             total_vds=form.total_vds.data,
#             total_payment=form.total_payment.data,
#             user_id=current_user.get_id()
#         )
#
#         db.session.add(data)
#         db.session.commit()
#
#         data_line = form.issue_vds_line.data
#         print(data_line)
#         line_data = json.loads(data_line)
#
#         vds_id = {"vds_id": data.id}
#         entry_date = {"entry_date": data.entry_date}
#         for i in range(len(line_data)):
#             line_data[i]["vds_id"] = vds_id["vds_id"]
#             line_data[i]["entry_date"] = entry_date["entry_date"]
#
#         # print(line_data)
#
#         for row in line_data:
#             print(row)
#             vds_line = [IssueVdsLine(**row)]
#             db.session.add_all(vds_line)
#             db.session.commit()
#
#     flash("VDS Issue Successfully")
#
#     return redirect(url_for('issue_vds.issue_vds_page'))
