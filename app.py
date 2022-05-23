from flask import Flask, render_template, redirect, session, flash, jsonify, request

from models import db, connect_db
# from forms import UserForm, EditCarForm
# from sqlalchemy.exc import IntegrityError


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///inventory_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)


@app.route('/')
def index():
    return 'hello world'
