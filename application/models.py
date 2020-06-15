from application import db, login_manager
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    phone_number = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String(500), nullable = False)
    office_address = db.relationship('Office_Locations', backref='full_address', lazy=True)
    
    def __repr__(self):
        return ''.join([
            'Primary Key ID: ', str(self.id), '\n', 
            'First Name: ', str(self.first_name), '\n',
            'Last Name: ', str(self.last_name), '\n',
            'Phone Number: ', str(self.phone_number), '\n',
            'Email: ', str(self.email), '\n', 
            'Password Hash', str(self.password), '\n',
            'office_address', str(self.office_address)
        ])

class Office_Locations(db.Model, UserMixin):
    location = db.Column(db.String(10), primary_key = True)
    first_line = db.Column(db.String(30), nullable = False)
    second_line = db.Column(db.String(30), nullable = True)
    post_code = db.Column(db.String(10), nullable = False)

    def __repr__(self):
        return ''.join([
            'Location: ', str(self.location), '\n', 
            'First Line: ', str(self.first_line), '\n'
            'Second Line: ', str(self.second_line), '\n', 
            'Post Code: ', str(self.post_code)
        ])