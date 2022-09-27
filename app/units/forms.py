from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


# Company Forms
class UnitsForm(FlaskForm):
    unit_name = StringField('unit_name', validators=[DataRequired()])
    short_name = StringField('short_name', validators=[DataRequired()])
