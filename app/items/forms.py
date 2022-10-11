from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

# Items Forms
itemType = [('1', 'Local'), ('2', 'Foreign')]


class ItemsForm(FlaskForm):
    item_name = StringField('item_name', validators=[DataRequired()])
    item_type = SelectField(u'item_type', choices=itemType)
    hs_code = StringField('hs_code', validators=[DataRequired()])
    hs_code_id = SelectField('hs_code_id', choices=[])
    unit_id = SelectField('unit_id', choices=[])
    stock_status = StringField('stock_status')
    status = StringField('status')
