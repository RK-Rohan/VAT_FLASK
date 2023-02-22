from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

# Items Forms
itemType = [('1', 'Service'), ('2', 'Finish Good')]


class ItemsForm(FlaskForm):
    item_name = StringField('item_name', validators=[DataRequired()])
    item_type = SelectField(u'item_type', choices=itemType)
    hs_code = SelectField('hs_code', choices=[], validators=[DataRequired()])
    hs_code_id = SelectField('hs_code_id', choices=[])
    unit_id = SelectField('unit_id', choices=[])
    stock_status = StringField('stock_status')
    status = StringField('status')
