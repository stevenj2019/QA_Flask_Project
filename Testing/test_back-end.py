import unittest
import os 

from urllib.request import urlopen

from flask import url_for
from flask_testing import TestCase

from application import app, db, bcrypt
from application.models import Admin, Contact, Locations


class TestBase(TestCase):

    def create_app(self):

        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI=os.getenv('TEST_DB_URI'),
            SECRET_KET=os.getenv('TEST_SECRET_KEY'), 
            WTF_CSRF_ENABLES=False,
            DEBUG=True
        )
        self.user = Admin(
            email='john@doe.com', 
            password=bcrypt.generate_password_hash('ThisPasswordSucks'))

        return app

    def setUp(self):

        db.session.commit()
        db.drop_all()
        db.create_all()

        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    #unauthenticated pages
    def test_auth_view(self):
        self.assertEqual(self.client.get(url_for(auth)), 200)
