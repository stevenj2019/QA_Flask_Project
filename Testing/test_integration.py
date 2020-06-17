import unittest
import time
import os

from flask import url_for
from flask_testing import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from urllib.request import urlopen

from application import app, db, bcrypt
from application.models import Admin

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('TEST_DATABASE'))
        app.config['SECRET_KEY'] = getenv('SKEY')
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path='../chromedriver', chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestLogin(TestBase):

    def test_login(self):
        user = Admin(
            email='john@doe.com', 
            password=bcrypt.generate_password_hash('ThisPasswordSucks'))

        self.driver.navigate().to(url_for(auth))
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(user.email)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(user.password)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        assert url_for('home') in self.driver.current_url