from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, DateField, DecimalField, IntegerField, DateTimeLocalField
from wtforms.validators import DataRequired


# Purchase Forms
class IssueVdsForm(FlaskForm):
    id = StringField('purchase_id')
    supplier_id = SelectField('supplier_id', choices=[], validators=[DataRequired()])
    purchase_invoice = SelectField('purchase_invoice', choices=[], validators=[DataRequired()])
    vds_no = StringField('vds_no', validators=[DataRequired()])
    vds_type = SelectField(u'vds_type', choices=[('1', 'Production'), ('2', 'Trading'), ('3', 'Service')])
    entry_date = DateField('entry_date', validators=[DataRequired()])
    total_amount = DecimalField('total_amount')
    total_vat = DecimalField('total_vat')
    total_vds = DecimalField('total_vds')
    total_payment = DecimalField('total_payment')
    user_id = IntegerField('user_id')
    issue_vds_line = StringField('issue_vds_line')

