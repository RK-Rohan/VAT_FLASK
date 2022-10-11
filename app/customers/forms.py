from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField
from wtforms.validators import DataRequired, Email


# Customers Forms
customerType = [('1', 'Local'), ('2', 'Foreign')]


class CustomersForm(FlaskForm):
    customer_name = StringField('customer_name', validators=[DataRequired()])
    email_address = EmailField('email_address', validators=[DataRequired(), Email()])
    phone_number = StringField('phone_number', validators=[DataRequired()])
    country_id = SelectField('country_id', choices=[])
    customer_type = SelectField(u'customer_type', choices=customerType)
    customer_address = StringField('customer_address', validators=[DataRequired()])
    shipping_address = StringField('shipping_address')
    shipping_country = SelectField('shipping_country', choices=[])
    customer_bin = StringField('customer_bin')
    customer_tin = StringField('customer_tin')
