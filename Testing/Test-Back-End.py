import unittest
import os 

from flask import url_for
from flask_testing import TestCase

from application import app, db, bcrypt
from application.models import Users, Office_Locations

class TestBase(TestCase):

    def create_app(self):

        config_name = 'testing'
        app,config.update(
            SQLALCHEMY_DATABASE_URI=os.getenv('TEST_DB_URI'),
            SECRET_KET=os.getenv('TEST_SECRET_KEY'), 
            WTF_CSRF_ENABLES=False,
            DEBUG=True
        )
        return app

    def setUp(self):

        db.session.commit()
        db.drop_all()
        db.create_all()

        admin = Users(
            first_name='admin',
            last_name='admin',
            phone_number='07627892126'
            email='admin@admin.com', 
            password=bcrypt.generate_password_hash('admin2016'),
            office_address='Manchester')

        user = Users(
            first_name='john',
            last_name='doe',
            phone_number='07627365426'
            email='john@doe.com', 
            password=bcrypt.generate_password_hash('ThisPasswordSucks'),
            office_address='London')
        )
        db.session.add(admin)
        db.session.add(user)
        db.session.commit()

        def tearDown(self):
            db.session.remove()
            db.drop_all()

class TestViews(TestBase):

    #unauthenticated pages
    def test_auth_view(self):
        self.assertEqual(self.client.get(url_for(auth)), 200)

    def test_home_view_noauth(self):
        self.assertEqual(self.client.get(url_for(home)), some_int)#find out error status for unauthenticated users

    #authenticated pages
    def test_home_view_auth(self):
        self.assertEqual(self.client.get(url_for(home)), 200)

class TestUsers(TestBase):

    def test_register(self):
        return False
    
    def test_login(self):
        return False

    def test_update(self):
        return False

    def test_delete(self):
        return False

class TestOtherUsers(TestBase):

    def test_searchByLocation(self):
        return False

    def test_searchByName(self):
        return False

    def test_userProfile(self):
        return False