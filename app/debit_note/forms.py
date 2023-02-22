from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, DateField, DecimalField, IntegerField, DateTimeLocalField
from wtforms.validators import DataRequired


# Purchase Forms
class DebitNoteForm(FlaskForm):
    debit_note_no = StringField('debit_note_no')
    supplier_id = SelectField('supplier_id', choices=[], validators=[DataRequired()])
    purchase_id = SelectField('purchase_id', choices=[], validators=[DataRequired()])
    vehicle_info = StringField('vehicle_info')
    debit_note_type = SelectField(u'debit_note_type', choices=[('1', 'Production'), ('2', 'Trading'), ('3', 'Service')])
    dn_issue_date = DateField('dn_issue_date', validators=[DataRequired()])
    total_payment = DecimalField('total_payment')
    user_id = IntegerField('user_id')
    debit_note_line = StringField('debit_note_line')

