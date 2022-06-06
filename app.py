
from flask import Flask, render_template, redirect, session, flash, jsonify, request
from flask_wtf.csrf import CSRFProtect


from models import db, connect_db
from forms import SearchForm
from yelpAPI import API_KEY, get_business_data
import requests

# from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

csrf = CSRFProtect(app)

app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///bite_finder_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)


@app.route('/', methods=["GET"])
def index():

    form = SearchForm()

    return render_template('index.html', form=form)


@app.route('/api/get-restaurant', methods=["POST"])
def get_restaurant():

    form = SearchForm()

    if form.validate_on_submit():
        zip_code = form.zip_code.data
        category = form.category.data
        radius = form.radius.data

        # print('********************')
        # print(zip_code, category, radius)
        # print('********************')

        business = get_business_data(zip_code, category, radius)
        return (business, 201)

    return redirect('/')
