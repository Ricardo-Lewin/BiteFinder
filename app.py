import os
import re

from flask import Flask, render_template, redirect, session, flash, g
from flask_wtf.csrf import CSRFProtect
from sqlalchemy.exc import IntegrityError
from models import db, connect_db, User
from forms import AnonSearchForm, UserSearchForm, UserAddForm, LoginForm, EditUserForm
from yelpAPI import get_business_data, user_get_business_data


CURR_USER_KEY = "curr_user"

app = Flask(__name__)

csrf = CSRFProtect(app)

uri = os.environ.get('DATABASE_URL', 'postgresql:///bite_finder_db')
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = os.environ.get('1234', "it's a secret")

connect_db(app)

db.create_all()

##############################################################################
# User signup/login/logout


@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:

        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""
    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


##############################################################################


@app.route('/', methods=["GET"])
def index():

    if g.user:
        form = UserSearchForm()
    else:
        form = AnonSearchForm()

    return render_template('index.html', form=form)


@app.route('/users/profile', methods=["GET", "POST"])
def edit_profile():
    """Show/Update profile for current user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    user = g.user
    form = EditUserForm(obj=user)

    if form.validate_on_submit():

        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.email = form.email.data

        db.session.commit()
        flash("Changes Made!", "success")
        return redirect("/users/profile")

    return render_template('users/edit.html', form=form, user_id=user.id)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle user signup.

    Create new user and add to DB. Redirect to home page.

    If form not valid, present form.

    If the there already is a user with that username: flash message
    and re-present form.
    """
    if g.user:

        return redirect('/')

    form = UserAddForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                password=form.password.data,
                email=form.email.data,
            )
            db.session.commit()

        except IntegrityError:
            flash("Account Already Created, Please Log In", 'danger')
            return render_template('users/signup.html', form=form)

        do_login(user)

        return redirect("/")

    else:
        return render_template('users/signup.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    if g.user:
        return redirect('/')

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.email.data,
                                 form.password.data)

        if user:
            do_login(user)
            flash(f"Welcome Back, {user.first_name}!", "success")
            return redirect("/")

        flash("Invalid credentials.", 'danger')

    return render_template('users/login.html', form=form)


@app.route('/logout')
def logout():
    """Handle logout of user."""
    if not g.user:
        return redirect("/")

    do_logout()
    flash("Goodbye!", "info")
    return redirect('/')


#### API ROUTES #######################################
@app.route('/api/anon-get-restaurant', methods=["POST"])
def anon_get_restaurant():
    """handles call from client side and returns business info"""

    form = AnonSearchForm()

    if form.validate_on_submit():
        try:

            zip_code = form.zip_code.data
            category = form.category.data
            radius = form.radius.data

            business = get_business_data(zip_code, category, radius)
            return (business, 201)
        except:
            flash("Invalid Zip Code", 'warning')
            return redirect('/')
    else:
        return("Form Error", form.errors)


@app.route('/api/user-get-restaurant', methods=["POST"])
def user_get_restaurant():
    """handles call from client side and returns business info"""

    form = UserSearchForm()

    if form.validate_on_submit():

        zip_code = form.zip_code.data
        category = form.category.data
        radius = form.radius.data
        price = form.price.data

        business = user_get_business_data(zip_code, category, radius, price)
        return (business, 201)


##############################################################################
