from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, DateField, DecimalField, IntegerField, DateTimeLocalField
from wtforms.validators import DataRequired


# Purchase Forms
class PayableMushakForm(FlaskForm):
    pay_type = SelectField(u'pay_type', choices=[
        ('25', 'Payment not Payment Through Bank(25)'),
        ('41', 'Interest on Overdue VAT(41)'),
        ('42', 'Interest on Overdue SD(42)'),
        ('43', 'Fine/penalty/interest(43)'),
        ('44', 'Others Fine/penalty/interest(44)'),
        ('45', 'Payable Excise Duty(45)'),
        ('46', 'Payable Development Surcharge(46)'),
        ('47', 'Payable ICT Development Surcharge(47)'),
        ('48', 'Payable Health Care Surcharge(48)'),
        ('49', 'Payable Environmental Protection Surcharge(49)'),
        ('52', 'Last Month Closing VAT(52)'),
        ('53', 'Last Month Closing SD(53)'),
        ('54', 'Remaining Balance VAT(54)'),
        ('55', 'Remaining Balance SD(55)'),
    ])
    pay_date = DateField('pay_date', validators=[DataRequired()])
    pay_amount = DecimalField('pay_amount')
    business_type = SelectField(u'business_type', choices=[('1', 'Service'), ('2', 'Finish Good'), ('3', 'Service')])
    created_at = DateTimeLocalField('created_at', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    user_id = IntegerField('user_id')

