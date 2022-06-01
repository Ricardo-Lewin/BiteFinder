from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerRangeField
from wtforms.validators import InputRequired


class SearchForm(FlaskForm):
    """Form for adding queries to search"""

    zip_code = StringField("Zip Code", validators=[InputRequired()])
    category = SelectField("Category", choices=[(
        "bbq", "Barbeque"), ("brazilian", "Brazilian"), ("breakfast & brunch", "Breakfast & Brunch"), ("burgers", "Burgers")])
    radius = IntegerRangeField("Distance in Miles")
