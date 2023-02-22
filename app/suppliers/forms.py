from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField
from wtforms.validators import DataRequired, Email


# Customers Forms
supplierType = [('1', 'Local'), ('2', 'Foreign')]


class SupplierForm(FlaskForm):
    supplier_name = StringField('supplier_name', validators=[DataRequired()])
    email_address = EmailField('email_address', validators=[DataRequired(), Email()])
    phone_number = StringField('phone_number', validators=[DataRequired()])
    country_id = SelectField('country_id', choices=[])
    supplier_type = SelectField(u'supplier_type', choices=supplierType)
    supplier_address = StringField('supplier_address', validators=[DataRequired()])
    supplier_bin = StringField('supplier_bin')
    supplier_tin = StringField('supplier_tin')
