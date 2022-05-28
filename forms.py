from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


class SearchForm(FlaskForm):
    """Form for adding queries to search"""

    zip_code = StringField("Zip Code", validators=[InputRequired()])
