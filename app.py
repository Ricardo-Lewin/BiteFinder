
from flask import Flask, render_template, redirect, session, flash, jsonify, request
from models import db, connect_db
from forms import SearchForm
from yelpAPI import API_KEY
import requests

# from sqlalchemy.exc import IntegrityError


app = Flask(__name__)

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
        # Create function that converts miles to meters
        print('********************')
        print(zip_code, category, radius)
        print('********************')

    return redirect('/')
