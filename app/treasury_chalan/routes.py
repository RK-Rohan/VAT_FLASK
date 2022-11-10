from flask import render_template, request, flash, redirect, url_for, json, jsonify
from flask_login import LoginManager, login_required, current_user
from datetime import date, datetime

from app import db
from treasury_chalan import treasury_chalan
from treasury_chalan.models import TreasuryChalan
from treasury_chalan.forms import TreasuryChalanForm

login_manager = LoginManager()


@treasury_chalan.route('/treasury_chalan/')
@login_required
def treasury_chalan_page():
    form = TreasuryChalanForm(request.form)
    result = TreasuryChalan.query.all()

    return render_template('treasury_chalan/index.html', treasury_chalan=result, form=form)


@treasury_chalan.route('/treasury_chalan/create/', methods=['GET', 'POST'])
def treasury_chalan_create():
    form = TreasuryChalanForm(request.form)

    return render_template('treasury_chalan/create.html', form=form)


@treasury_chalan.route('/treasury_chalan/store/', methods=['GET', 'POST'])
def treasury_chalan_store():
    form = TreasuryChalanForm(request.form)

    if 'treasury_store' in request.form:
        data = TreasuryChalan(
            t_chalan_no=form.t_chalan_no.data,
            t_bank=form.t_bank.data,
            t_branch=form.t_branch.data,
            t_account_code=form.t_account_code.data,
            t_amount=form.t_amount.data,
            t_date=form.t_date.data,
            execute_date=form.execute_date.data,
            t_type=form.t_type.data,
            business_type=form.business_type.data,
            created_at=datetime.now(),
            user_id=current_user.get_id()
        )

        db.session.add(data)
        db.session.commit()

    flash("Treasury Chalan Store Successfully")

    return redirect(url_for('treasury_chalan.treasury_chalan_page'))

