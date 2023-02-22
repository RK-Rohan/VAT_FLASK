from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, DateField, DecimalField, IntegerField, DateTimeLocalField
from wtforms.validators import DataRequired


# Purchase Forms
class ReceiveVdsForm(FlaskForm):
    id = StringField('purchase_id')
    customer_id = SelectField('customer_id', choices=[], validators=[DataRequired()])
    sales_invoice = SelectField('sales_invoice', choices=[], validators=[DataRequired()])
    vds_no = StringField('vds_no', validators=[DataRequired()])
    vds_type = SelectField(u'vds_type', choices=[('1', 'Production'), ('2', 'Trading'), ('3', 'Service')])
    entry_date = DateField('entry_date', validators=[DataRequired()])
    vds_certificate_no = StringField('vds_certificate_no', validators=[DataRequired()])
    receive_date = DateField('receive_date', validators=[DataRequired()])
    total_amount = DecimalField('total_amount')
    total_vat = DecimalField('total_vat')
    total_vds = DecimalField('total_vds')
    total_receive = DecimalField('total_receive')
    user_id = IntegerField('user_id')
    receive_vds_line = StringField('issue_vds_line')

