from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, DateField, DecimalField, IntegerField, DateTimeLocalField
from wtforms.validators import DataRequired


# Purchase Forms
class SalesForm(FlaskForm):
    id = StringField('purchase_id')
    customer_id = SelectField('customer_id', choices=[], validators=[DataRequired()])
    customer_address = StringField('customer_address', render_kw={'readonly': True})
    sale_date = DateField('sale_date', validators=[DataRequired()])
    sales_invoice = StringField('sales_invoice')
    vehicle_info = StringField('vehicle_info')
    destination = StringField('destination')
    sales_challan = StringField('sales_challan')
    # challan_date = DateTimeLocalField('challan_date', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    sales_type = SelectField(u'sales_type', choices=[('1', 'Service'), ('2', 'Finish Good'), ('3', 'Service')])
    total_discount = DecimalField('total_discount')
    total_sd = DecimalField('total_sd')
    total_vat = DecimalField('total_vat')
    grand_total = DecimalField('grand_total')
    notes = StringField('notes')
    user_id = IntegerField('user_id')
    sales_line = StringField('sales_line')


class SalesLine(FlaskForm):
    item_id = DecimalField('items_id')
    hs_code_id = StringField('hs_code_id')
    qty = StringField('qty')
    rate = DecimalField('rate')
    rate_value = DecimalField('rate_value')
