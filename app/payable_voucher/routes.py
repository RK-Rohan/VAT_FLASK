from flask import render_template, request, flash, redirect, url_for, json, jsonify
from flask_login import LoginManager, login_required, current_user
from datetime import date, datetime

from app import db
from payable_voucher import payable_voucher
from payable_voucher.models import PayableVoucher
from payable_voucher.forms import PayableVoucherForm

login_manager = LoginManager()


@payable_voucher.route('/payable_voucher/')
@login_required
def payable_voucher_page():
    form = PayableVoucherForm(request.form)
    result = PayableVoucher.query.all()

    return render_template('payable_voucher/index.html', payable_voucher=result, form=form)


@payable_voucher.route('/payable_voucher/create/', methods=['GET', 'POST'])
def payable_voucher_create():
    form = PayableVoucherForm(request.form)

    return render_template('payable_voucher/create.html', form=form)


@payable_voucher.route('/payable_voucher/store/', methods=['GET', 'POST'])
def payable_voucher_store():
    form = PayableVoucherForm(request.form)

    if 'payable_voucher_store' in request.form:
        data = PayableVoucher(
            payable_desc=form.payable_desc.data,
            chalan_no=form.chalan_no.data,
            payable_amount=form.payable_amount.data,
            vat_amount=form.vat_amount.data,
            chalan_date=form.chalan_date.data,
            execute_date=form.execute_date.data,
            business_type='3',
            created_at=datetime.now(),
            user_id=current_user.get_id()
        )

        db.session.add(data)
        db.session.commit()

    flash("Payable Voucher Store Successfully")

    return redirect(url_for('payable_voucher.payable_voucher_page'))

