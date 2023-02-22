from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, DateField, DecimalField, IntegerField, DateTimeLocalField
from wtforms.validators import DataRequired


# Purchase Forms
class PayableVoucherForm(FlaskForm):
    chalan_no = StringField('chalan_no', validators=[DataRequired()])
    payable_desc = StringField('payable_desc', validators=[DataRequired()])
    payable_amount = DecimalField('payable_amount')
    vat_amount = DecimalField('vat_amount')
    chalan_date = DateField('chalan_date', validators=[DataRequired()])
    execute_date = DateField('execute_date', validators=[DataRequired()])
    business_type = SelectField(u'business_type', choices=[('1', 'Service'), ('2', 'Finish Good'), ('3', 'Service')])
    created_at = DateTimeLocalField('created_at', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    user_id = IntegerField('user_id')

