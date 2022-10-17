from flask import render_template, request, flash, redirect, url_for, jsonify
from flask_login import LoginManager, login_required

from items import items
from app import db
from items.models import Items, HSCode, ItemSchema
from items.forms import ItemsForm

from units.models import Units
from units.forms import UnitsForm

login_manager = LoginManager()


@items.route('/items/')
def items_page():
    form = ItemsForm(request.form)
    # result = Items.query.all()
    result = db.session.execute(
        "SELECT items.*, hs_code.hs_code, units.unit_name "
        "FROM `items` "
        "JOIN units ON items.unit_id = units.id "
        "JOIN hs_code  ON items.hs_code = hs_code.id "
    )

    return render_template('items/index.html', items=result, form=form)


@items.route('/items/create/', methods=['GET', 'POST'])
def items_create():
    form = ItemsForm(request.form)
    unitsform = UnitsForm(request.form)
    form.unit_id.choices = [(units.id, units.unit_name) for units in Units.query.all()]
    form.hs_code.choices = [(hs_code.id, hs_code.hs_code) for hs_code in HSCode.query.all()]
    hs_code = HSCode.query.all()

    return render_template('items/create.html', form=form, hs_code=hs_code, units=unitsform)


@items.route('/items/store/', methods=['GET', 'POST'])
def items_store():
    form = ItemsForm(request.form)
    # hs_code_id = form.hs_code.data
    # hs_code = db.session.execute("SELECT hs_code FROM hs_code WHERE id = %s", [hs_code_id])

    if 'item_create' in request.form:
        data = Items(
            item_name=form.item_name.data,
            unit_id=form.unit_id.data,
            hs_code=form.hs_code.data,
            hs_code_id=form.hs_code.data,
            item_type=form.item_type.data,
        )
        db.session.add(data)
        db.session.commit()
    flash("Item Inserted Successfully")

    return redirect(url_for('items.items_page'))


@items.route('/api/items/',  methods=['GET', 'POST'])
def item_list():
    # item_lists = Items.query.all()
    item_lists = db.session.execute(
        "SELECT items.*, hs_code.sd, hs_code.vat "
        "FROM `items`"
        "JOIN hs_code ON items.hs_code_id = hs_code.id "
    )
    item_schema = ItemSchema()
    output = item_schema.dump(item_lists, many=True)
    return jsonify({'items': output})


@items.route('/api/items/<itemid>/', methods=['GET', 'POST'])
def item_details(itemid):
    # item_lists = Items.query.get(id)
    itemList = Items.query.join(HSCode, Items.hs_code_id == HSCode.id)\
        .add_columns\
        (
            Items.id,
            Items.item_name,
            Items.item_type,
            Items.hs_code_id,
            Items.unit_id,
            HSCode.hs_code,
            HSCode.sd,
            HSCode.vat
        ).filter(Items.id == itemid)

    item_schema = ItemSchema()
    output = item_schema.dump(itemList, many=True)
    return jsonify({'items': output})


@items.route('/api/items/terms/<term>/', methods=['GET', 'POST'])
def item_term(term):
    # item_lists = Items.query.get(id)
    itemList = Items.query.join(HSCode, Items.hs_code_id == HSCode.id)\
        .add_columns\
        (
            Items.id,
            Items.item_name,
            Items.item_type,
            Items.hs_code_id,
            Items.unit_id,
            HSCode.hs_code,
            HSCode.sd,
            HSCode.vat
        ).filter(Items.item_name.ilike("%" + term + "%"))
    print(itemList)
    item_schema = ItemSchema()
    output = item_schema.dump(itemList, many=True)
    return jsonify({'items': output})
