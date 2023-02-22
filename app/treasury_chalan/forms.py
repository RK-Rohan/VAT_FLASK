from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, DateField, DecimalField, IntegerField, DateTimeLocalField
from wtforms.validators import DataRequired


# Purchase Forms
class TreasuryChalanForm(FlaskForm):
    t_chalan_no = StringField('t_chalan_no', validators=[DataRequired()])
    t_bank = StringField('t_bank', validators=[DataRequired()])
    t_branch = StringField('t_branch', validators=[DataRequired()])
    t_account_code = StringField('t_account_code', validators=[DataRequired()])
    t_amount = DecimalField('t_amount')
    t_date = DateField('t_date', validators=[DataRequired()])
    execute_date = DateField('execute_date', validators=[DataRequired()])
    t_type = SelectField(u't_type', choices=[
        ('58', 'VAT Deposit'),
        ('59', 'SD Deposit'),
        ('60', 'Excise Duty'),
        ('61', 'Development Surcharge'),
        ('62', 'ICT Development Surcharge'),
        ('63', 'Health Care Surcharge'),
        ('64', 'Environmental Protection Surcharge')
    ])
    business_type = SelectField(u'business_type', choices=[('1', 'Service'), ('2', 'Finish Good'), ('3', 'Service')])
    created_at = DateTimeLocalField('created_at', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    user_id = IntegerField('user_id')

