from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, DateField, DecimalField, IntegerField, DateTimeLocalField
from wtforms.validators import DataRequired


# Purchase Forms
class CreditNoteForm(FlaskForm):
    credit_note_no = StringField('credit_note_no')
    customer_id = SelectField('customer_id', choices=[], validators=[DataRequired()])
    sales_id = SelectField('sales_id', choices=[], validators=[DataRequired()])
    vehicle_info = StringField('vehicle_info')
    credit_note_type = SelectField(u'credit_note_type', choices=[('1', 'Production'), ('2', 'Trading'), ('3', 'Service')])
    cn_issue_date = DateField('cn_issue_date', validators=[DataRequired()])
    total_payment = DecimalField('total_payment')
    user_id = IntegerField('user_id')
    credit_note_line = StringField('credit_note_line')

