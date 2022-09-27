from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField
from wtforms.validators import Email, DataRequired


# Company Forms
Vat_type = [('1', 'Deducted'), ('2', 'Not Deducted')]
Currency = [('1', 'Taka'), ('2', 'US Dollar'), ('3', 'Yuan'), ('4', 'Ruble')]


class CompanyForm(FlaskForm):
    company_name = StringField('company_name', validators=[DataRequired()])
    short_name = StringField('short_name', validators=[DataRequired()])
    email_address = EmailField('email_address', validators=[DataRequired(), Email()])
    phone_number = StringField('phone_number', validators=[DataRequired()])
    country = SelectField('country', choices=[])
    address = StringField('address', validators=[DataRequired()])
    invoice_logo = StringField('invoice_logo', validators=[DataRequired()])
    bank_name = StringField('bank_name', validators=[DataRequired()])
    ac_number = StringField('ac_number', validators=[DataRequired()])
    branch = StringField('branch', validators=[DataRequired()])
    business_nature = StringField('business_nature', validators=[DataRequired()])
    business_economics = StringField('business_economics', validators=[DataRequired()])
    vat_type = SelectField(u'vat_type', choices=Vat_type)
    bin_number = StringField('bin_number', validators=[DataRequired()])
    tin_number = StringField('tin_number', validators=[DataRequired()])
    currency = SelectField(u'currency', choices=Currency)
    person_name = StringField('person_name', validators=[DataRequired()])
    designation = StringField('designation', validators=[DataRequired()])
    person_phone_number = StringField('person_phone_number', validators=[DataRequired()])
    nid = StringField('nid', validators=[DataRequired()])
    person_email = StringField('person_email', validators=[DataRequired()])

