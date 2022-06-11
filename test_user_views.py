# run these tests like:
#
#    FLASK_ENV=production python -m unittest test_message_views.py

from unittest import TestCase
from app import app
import os

from models import db, connect_db, User
from bs4 import BeautifulSoup

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///bitefinder-test"

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()


# Don't have WTForms use CSRF at all, since it's a pain to test

app.config['WTF_CSRF_ENABLED'] = False


#########VIEW ROUTE TESTS#############


class UserViewsTestCase(TestCase):
    """Tests user views."""

    def test_main_page(self):
        """Test GET on home page"""

        with app.test_client() as client:
            # can now make requests to flask via `client` simulates server without having to start one up for tests
            resp = client.get('/')   # gets http response
            html = resp.get_data(as_text=True)   # pulls data form responses

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h2>Can't Decide What To Eat?</h2>", html)

    def test_sign_up_form(self):
        """Test GET on sign up page"""
        with app.test_client() as client:
            resp = client.get('/signup')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h2>Join BiteFinder today.</h2>", html)

    def test_sign_up_post(self):
        """Test POST on sign up page"""
        with app.test_client() as client:
            resp = client.post("/signup", data={
                "first_name": "first",
                "last_name": "last",
                "email": "test@gmail.com",
                "password": "password1"
            })
            assert resp.status_code == 200

    def test_login_form(self):
        """Test GET on login page"""
        with app.test_client() as client:
            resp = client.get('/login')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h2>Welcome back.</h2>", html)

    def test_login_post(self):
        """Test POST on login page"""
        with app.test_client() as client:
            resp = client.post("/login", data={
                "email": "test@gmail.com",
                "password": "password1"
            })
            assert resp.status_code == 200

    def test_api_post(self):
        """Tests api route"""
        with app.test_client() as client:
            resp = client.post("/api/get-restaurant", data={
                "zip_code": "30303",
                "category": "barbeque",
                "radius": 10
            })
            assert resp.status_code == 200

        # test for login func

        # test for logout func
        ########################################

        ###########JS tests###################
        # test for handleresponse

        # test for do_login

        # test for do_logout

        # randomize

        # show card

        # fail card

        # test for ajax request
