from application import db, login_manager
from flask_login import UserMixin

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String(500), nullable = False)
    
    def __repr__(self):
        return ''.join([
            'Email: ', str(self.email), '\n', 
            'Password Hash', str(self.password), '\n',
        ])

class Connect(db.Model):
    contact_id = db.Column('contact_id', db.Integer, db.ForeignKey('contact.contact_id'), primary_key = True),
    location_id = db.Column('location_id', db.Integer, db.ForeignKey('locations.location_id'))

class Contact(db.Model):
    contact_id = db.Column(db.Integer, primary_key = True)    
    first_name = db.Column(db.String(10), nullable = False)
    last_name = db.Column(db.String(20), nullable = False)
    email_address = db.Column(db.String(30), nullable = False)
    phone_number = db.Column(db.String(15), nullable = False)
    office_locations = db.relationship('Locations', secondary='Connect', backref=db.backref('Occupants', lazy='dynamic'))

class Locations(db.Model):
    location_id = db.Column(db.Integer, primary_key = True)
    first_line = db.Column(db.String(15), nullable = False)
    second_line = db.Column(db.String(15), nullable = True)
    city = db.Column(db.String(15), nullable = False)
    post_code = db.Column(db.String(10), nullable = False)
    occupants = db.relationship('Contact', secondary='Connect', backref=db.backref('Address', lazy='dynamic'))

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))