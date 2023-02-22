from flask import render_template, request, flash, redirect, url_for, json, jsonify
from flask_login import LoginManager, login_required, current_user
from datetime import date, datetime

from app import db
from receivable_voucher import receivable_voucher
from receivable_voucher.models import ReceivableVoucher
from receivable_voucher.forms import ReceivableVoucherForm

login_manager = LoginManager()


@receivable_voucher.route('/receivable_voucher/')
@login_required
def receivable_voucher_page():
    form = ReceivableVoucherForm(request.form)
    result = ReceivableVoucher.query.all()

    return render_template('receivable_voucher/index.html', receivable_voucher=result, form=form)


@receivable_voucher.route('/receivable_voucher/create/', methods=['GET', 'POST'])
def receivable_voucher_create():
    form = ReceivableVoucherForm(request.form)

    return render_template('receivable_voucher/create.html', form=form)


@receivable_voucher.route('/receivable_voucher/store/', methods=['GET', 'POST'])
def receivable_voucher_store():
    form = ReceivableVoucherForm(request.form)

    if 'receivable_voucher_store' in request.form:
        data = ReceivableVoucher(
            receivable_desc=form.receivable_desc.data,
            chalan_no=form.chalan_no.data,
            receivable_amount=form.receivable_amount.data,
            vat_amount=form.vat_amount.data,
            chalan_date=form.chalan_date.data,
            execute_date=form.execute_date.data,
            business_type='3',
            created_at=datetime.now(),
            user_id=current_user.get_id()
        )

        db.session.add(data)
        db.session.commit()

    flash("Receivable Voucher Store Successfully")

    return redirect(url_for('receivable_voucher.receivable_voucher_page'))

