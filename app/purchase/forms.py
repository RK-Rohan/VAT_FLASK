from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, DateField, DecimalField, IntegerField, DateTimeLocalField
from wtforms.validators import DataRequired


# Purchase Forms
class PurchaseForm(FlaskForm):
    supplier_id = SelectField('supplier_id', choices=[], validators=[DataRequired()])
    supplier_address = StringField('supplier_address', render_kw={'readonly': True})
    entry_date = DateTimeLocalField('entry_date', format='%m/%d/%y', validators=[DataRequired()])
    p_invoice_no = StringField('p_invoice_no', validators=[DataRequired()])
    purchase_type = SelectField(u'purchase_type', choices=[('1', 'Service'), ('2', 'Finish Good'), ('3', 'Service')])
    challan_no = StringField('challan_no', validators=[DataRequired()])
    challan_date = DateField('challan_date', validators=[DataRequired()])
    fiscal_year = SelectField(u'fiscal_year', choices=[('1', '2021'), ('2', '2022')])
    item_name = StringField('item_name')
    total_vds = DecimalField('total_vds')
    grand_total = DecimalField('grand_total')
    total_tax = DecimalField('total_tax')
    lc_date = DateField('lc_date', validators=[DataRequired()])
    lc_no = StringField('lc_no')
    custom_house = SelectField('custom_house', choices=[])
    country_origin = SelectField('country_origin', choices=[])
    data_source = SelectField('data_source', choices=[])
    cpc_code_id = SelectField('cpc_code_id', choices=[])
    boe_item_no = IntegerField('boe_item_no')
    notes = TextAreaField('notes')
    user_id = IntegerField('user_id')
