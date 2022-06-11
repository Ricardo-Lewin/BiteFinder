from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerRangeField, PasswordField
from wtforms.validators import InputRequired, DataRequired, Email, Length


class AnonSearchForm(FlaskForm):
    """Form for adding queries to search"""

    zip_code = StringField("Zip Code", validators=[InputRequired()])
    category = SelectField("Category", choices=[(
        "bbq", "Barbeque"), ("brazilian", "Brazilian"), ("breakfast & brunch", "Breakfast & Brunch"), ("burgers", "Burgers"), ("buffets", "Buffets"), ("cafes", "Cafes"), ("chinese", "Chinese"), ("cuban", "Cuban"),  ("fast food", "Fast Food"),  ("indian", "Indian"),  ("italian", "Italian"), ("japanese", "Japanese"), ("korean", "Korean"), ("mediterranean", "Mediterranean"), ("mexican", "Mexican"), ("middle eastern", "Middle Eastern"), ("peruvian", "Peruvian"), ("pizza", "Pizza"), ("seafood", "Seafood"), ("sushi", "Sushi"), ("thai", "Thai"), ("vegan", "Vegan"), ("vietnamese", "Vietnamese")])
    radius = IntegerRangeField("Distance in Miles")


class UserSearchForm(FlaskForm):
    """Form for adding queries to search"""

    zip_code = StringField("Zip Code", validators=[InputRequired()])
    category = SelectField("Category", choices=[(
        "bbq", "Barbeque"), ("brazilian", "Brazilian"), ("breakfast & brunch", "Breakfast & Brunch"), ("burgers", "Burgers"), ("buffets", "Buffets"), ("cafes", "Cafes"), ("chinese", "Chinese"), ("cuban", "Cuban"),  ("fast food", "Fast Food"),  ("indian", "Indian"),  ("italian", "Italian"), ("japanese", "Japanese"), ("korean", "Korean"), ("mediterranean", "Mediterranean"), ("mexican", "Mexican"), ("middle eastern", "Middle Eastern"), ("peruvian", "Peruvian"), ("pizza", "Pizza"), ("seafood", "Seafood"), ("sushi", "Sushi"), ("thai", "Thai"), ("vegan", "Vegan"), ("vietnamese", "Vietnamese")])
    price = SelectField(
        "Price", choices=[(1, "$"), (2, "$$"), (3, '$$$'), (4, '$$$$')])
    radius = IntegerRangeField("Distance in Miles")


class UserAddForm(FlaskForm):
    """Form for adding users."""

    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])


class EditUserForm(FlaskForm):
    """Edit User Form"""
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])


class LoginForm(FlaskForm):
    """Login form."""

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
