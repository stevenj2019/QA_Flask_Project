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

class Locations(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_line = db.Column(db.String(15), nullable = False)
    second_line = db.Column(db.String(15), nullable = True)
    post_code = db.Column(db.String(10), nullable = False)
    occupants = db.relationship('Contacts', backref='Users', lazy=True)

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key = True)    
    first_name = db.Column(db.String(10), nullable = False)
    last_name = db.Column(db.String(20), nullable = False)
    email_address = db.Column(db.String(30), nullable = False)
    phone_number = db.Column(db.String(15), nullable = False)
    office_location = db.Column(db.Integer, db.ForeignKey('Locations.id'), nullable = False)

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))