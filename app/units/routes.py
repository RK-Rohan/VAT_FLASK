from flask import render_template, request, flash, redirect, url_for
from flask_login import LoginManager, login_required

from units import units
from app import db
from units.models import Units
from units.forms import UnitsForm

login_manager = LoginManager()


@units.route('/units/')
def units_page():
    form = UnitsForm(request.form)
    all_data = Units.query.all()
    return render_template('units/index.html', units=all_data, form=form)


@units.route('/units/create', methods=['GET', 'POST'])
@login_required
def units_create():
    form = UnitsForm(request.form)
    if 'add_unit' in request.form:
        data = Units(
            unit_name=form.unit_name.data,
            short_name=form.short_name.data
        )
        db.session.add(data)
        db.session.commit()

        flash("Unit Inserted Successfully")
    return redirect(url_for('units.units_page'))


@units.route('/items/units', methods=['GET', 'POST'])
def items_unit():
    form = UnitsForm(request.form)
    if 'add_unit' in request.form:
        data = Units(
            unit_name=form.unit_name.data,
            short_name=form.short_name.data
        )
        db.session.add(data)
        db.session.commit()

        flash("Unit Inserted Successfully")
    return redirect(url_for('items.items_create'))


@units.route('/units/update', methods=['GET', 'POST'])
def units_update():

    if request.method == 'POST':
        data = Units.query.get(request.form.get('id'))

        data.unit_name = request.form['unit_name']
        data.short_name = request.form['short_name']

        db.session.commit()
        flash("Units Updated Successfully")

        return redirect(url_for('units.units_page'))

