import unittest
import time
import os

from flask import url_for
from flask_testing import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from urllib.request import urlopen

from application import app, db, bcrypt
from application.models import Admin, Contact, Locations

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('TEST_DB_URI'))
        app.config['SECRET_KEY'] = str(os.getenv('TEST_SECRET_KEY'))
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=os.getcwd()+'/chromedriver', chrome_options=chrome_options)
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
        db.session.add(user)
        db.session.commit()

        self.driver.find_element_by_xpath('/html/body/div/ul/li[4]/a').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(user.email)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('ThisPasswordSucks')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        assert url_for('home') in self.driver.current_url

class TestNewContact(TestBase):

    def test_new(self):
        contact = Contact(
            first_name = 'John',
            last_name = 'Johnson',
            email_address = 'john@johnson.john',
            phone_number = '+446251893271',
            location_id = None
        )
        self.driver.find_element_by_xpath('/html/body/div/ul/li[3]/a').click() #still need to add the click to the new page (requires auth)
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(contact.first_name)
        self.driver.find_element_by_xpath('//*[@id="last_name"]').send_keys(contact.last_name)
        self.driver.find_element_by_xpath('//*[@id="email_address"]').send_keys(contact.email_address)
        self.driver.find_element_by_xpath('//*[@id="phone_number"]').send_keys(contact.phone_number)
        self.driver.find_element_by_xpath('//*[@id="city"]').send_keys('Manchester')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        assert url_for('home') in self.driver.current_url