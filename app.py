import requests
import zipcodes

from flask import Flask, render_template, redirect, session, flash, g
from flask_wtf.csrf import CSRFProtect
from sqlalchemy.exc import IntegrityError
from models import db, connect_db, User
from forms import SearchForm, UserAddForm, LoginForm
from yelpAPI import API_KEY, get_business_data


CURR_USER_KEY = "curr_user"

app = Flask(__name__)

csrf = CSRFProtect(app)

app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///bite_finder_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)


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
    
    session['CURR_USER_KEY'] = user.id
    print(CURR_USER_KEY)

def do_logout():
    """Logout user."""
    print('line 47', session['CURR_USER_KEY'])
    if session['CURR_USER_KEY'] != "curr_user":
        del session['CURR_USER_KEY']
        

##############################################################################


@app.route('/', methods=["GET"])
def index():

    form = SearchForm()

    return render_template('index.html', form=form)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle user signup.

    Create new user and add to DB. Redirect to home page.

    If form not valid, present form.

    If the there already is a user with that username: flash message
    and re-present form.
    """

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

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.email.data,
                                 form.password.data)

        if user:
            do_login(user)
            flash(f"Hello, {user.first_name}!", "success")
            return redirect("/")

        flash("Invalid credentials.", 'danger')

    return render_template('users/login.html', form=form)


@app.route('/logout')
def logout():
    """Handle logout of user."""

    do_logout()
    flash("Goodbye!", "info")
    return redirect('/')


#### API ROUTES #######################################
@app.route('/api/get-restaurant', methods=["POST"])
def get_restaurant():
    """handles call from client side and returns business info"""
    form = SearchForm()

    if form.validate_on_submit():
        while True:
            try:
                zip_code = form.zip_code.data
                category = form.category.data
                radius = form.radius.data

                print("line 142",zipcodes.is_real(zip_code))

                business = get_business_data(zip_code, category, radius)
                return (business, 201)
            except:
                flash("Invalid Zip Code", 'warning')
                return redirect('/')


##############################################################################