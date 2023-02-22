from flask import render_template, request, flash, redirect, url_for, json, jsonify
from flask_login import LoginManager, login_required, current_user
from datetime import date, datetime

from app import db
from payable_91 import payable_91
from payable_91.models import PayableMushak
from payable_91.forms import PayableMushakForm

login_manager = LoginManager()


@payable_91.route('/payable_91/')
@login_required
def payable_91_page():
    form = PayableMushakForm(request.form)
    result = PayableMushak.query.all()

    return render_template('payable_91/index.html', payable_mushak=result, form=form)


@payable_91.route('/payable_91/create/', methods=['GET', 'POST'])
def payable_91_create():
    form = PayableMushakForm(request.form)

    return render_template('payable_91/create.html', form=form)


@payable_91.route('/payable_91/store/', methods=['GET', 'POST'])
def payable_91_store():
    form = PayableMushakForm(request.form)

    if 'payable_91_store' in request.form:
        data = PayableMushak(
            pay_type=form.pay_type.data,
            pay_date=form.pay_date.data,
            pay_amount=form.pay_amount.data,
            business_type='3',
            created_at=datetime.now(),
            user_id=current_user.get_id()
        )

        db.session.add(data)
        db.session.commit()

    flash("Payable Mushak Store Successfully")

    return redirect(url_for('payable_91.payable_91_page'))

