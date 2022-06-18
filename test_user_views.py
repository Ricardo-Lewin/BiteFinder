# run these tests like:
#
#    FLASK_ENV=production python -m unittest test_user_views.py

from unittest import TestCase
from app import app, CURR_USER_KEY
import os

from models import db, connect_db, User


# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///test_bitefinder"

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()


# Don't have WTForms use CSRF at all, since it's a pain to test

app.config['WTF_CSRF_ENABLED'] = False


#########VIEW ROUTE TESTS#############


class UserViewsTestCase(TestCase):
    """Tests user views."""

    def setUp(self):
        """Create test client, add sample data."""

        db.drop_all()
        db.create_all()

        self.client = app.test_client()

        self.testuser = User.signup(first_name="testuser", last_name="testuser1",
                                    email="test@test.com",
                                    password="testpass")
        self.testuser_id = 8989
        self.testuser.id = self.testuser_id

        db.session.commit()

    def tearDown(self):
        resp = super().tearDown()
        db.session.rollback()
        return resp

    def test_main_page(self):
        """Test GET on home page"""

        with self.client as client:
            # can now make requests to flask via `client` simulates server without having to start one up for tests
            resp = client.get('/')   # gets http response
            html = resp.get_data(as_text=True)   # pulls data form responses

            self.assertEqual(resp.status_code, 200)
            self.assertIn(
                "<p>Pick a random food spot near you just with the click of a button!</p>", html)

    def test_sign_up_form(self):
        """Test GET on sign up page"""
        with self.client as client:
            resp = client.get('/signup')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn(
                '<h2 class="join-message">Join BiteFinder today.</h2>', html)

    def test_sign_up_post(self):
        """Test POST on sign up page"""

        with self.client as client:
            new_user = {'first_name': 'test2',
                        'last_name': 'testlast2',
                        'email': 'test2@gmail.com',
                        'password': 'postpass'}

            resp = client.post("/signup", data=new_user)

            self.assertEqual(resp.status_code, 302)

    def test_user_profile(self):
        """Test User Details page"""
        with self.client as client:
            with client.session_transaction() as session:
                session[CURR_USER_KEY] = self.testuser_id

            resp = client.get('/users/profile')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(
                '<h2 class="join-message">Edit Your Profile.</h2>', html)

    def test_login_form(self):
        """Test GET on login page"""
        with self.client as client:

            resp = client.get('/login')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(
                '<h2 class="join-message">Welcome back.</h2>', html)

    def test_login_post(self):
        """Test POST on login page"""
        with self.client as client:
            resp = client.post("/login", data={
                "email": "test@gmail.com",
                "password": "password1"
            })
            assert resp.status_code == 200

    def test_anon_api_post(self):
        """Tests api route"""
        with self.client as client:
            resp = client.post("/api/anon-get-restaurant", data={
                "zip_code": "30303",
                "category": "bbq",
                "radius": 10
            })
            assert resp.status_code == 201

    def test_user_api_post(self):
        """Tests api route"""
        with self.client as client:
            resp = client.post("/api/anon-get-restaurant", data={
                "zip_code": "30303",
                "category": "bbq",
                "radius": 10,
                "price": 2})
            assert resp.status_code == 201
