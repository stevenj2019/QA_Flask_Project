import unittest
import time
import os 

from urllib.request import urlopen

from flask import url_for
from flask_testing import TestCase
from flask_testing import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from application import app, db, bcrypt
from application.models import Admin, Contact, Office_Locations


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

        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser" 
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")

        db.session.add(admin)
        db.session.add(user)
        db.session.commit()

        def tearDown(self):
            self.driver.quit()
            print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")
            db.session.remove()
            db.drop_all()

        def test_server_is_alive(self):
            response = urlopen("http://localhost:5000")
            self.assertEqual(response.code, 200)
   

class TestViews(TestBase):

    #unauthenticated pages
    def test_auth_view(self):
        self.assertEqual(self.client.get(url_for(auth)), 200)

class TestUsers(TestBase):
    
    def test_login(self):
        self.driver.navigate().to(url_for(auth))
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys()
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys()
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        assert url_for('home') in self.driver.current_url