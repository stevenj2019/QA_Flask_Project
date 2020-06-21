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

        self.contact = Contact(
            first_name= 'John', 
            last_name= 'Johnson', 
            email_address= 'john@johnson.com', 
            phone_number= '+446789261532', 
            location_id = 1
        )
        self.location = Locations(
            first_line = 'number 1', 
            second_line = 'some street', 
            city = 'Manchester', 
            post_code = 'AAA1 AAA'
        )
        return app

    def setUp(self):

        db.session.commit()
        db.drop_all()
        db.create_all()

        db.session.add(self.location)
        db.session.add(self.user)
        db.session.add(self.contact)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_view(self):
        self.assertEqual(self.client.get(url_for('home')).status_code, 200)

    def test_new_contact_view(self):
        self.assertEqual(self.client.get(url_for('new')).status_code, 200) 

    def test_auth_view(self):
        self.assertEqual(self.client.get(url_for('auth')).status_code, 200)
 
    def test_edit_view(self):
        self.assertEqual(self.client.get(url_for('edit', user_id=1)).status_code, 200)

class TestDb(TestBase):
    
    def test_user(self):

        with self.client:
            response = self.client.post(
                '/newcontact',
                data = dict(
                   first_name = 'john',
                   last_name = 'johnson',
                   email_address = 'john@johnson.com',
                   phone_number = '+446168952173',
                   location_id = 1
                ), 
            follow_redirects=True
            )
        self.assertIn(b'john', response.data)
        self.assertIn(b'johnson', response.data)
        self.assertIn(b'john@johnson.com', response.data)
        self.assertIn(b'+446168952173', response.data)