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

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(10), nullable = False)
    last_name = db.Column(db.String(20), nullable = False)
    email_address = db.Column(db.String(30), nullable = False)
    phone_number = db.Column(db.String(15), nullable = False)
    office_location = db.relationship('Office_Locations', backref='Address', lazy=True)
    
    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\n',
            'First Name: ', str(self.first_name), '\n',
            'Last Name: ', str(self.last_name), '\n',
            'Email Address: ', str(self.email_address), '\n',
            'Phone Number: ', str(self.phone_number), '\n',
            'Office Location', str(self.office_location), '\n'
        ])

class Office_Locations(db.Model, UserMixin):
    id = db.Column(db.Integer, nullable = False)
    city = db.column(db.string(15), db.ForeignKey('Contact.office_location'), nullable = False)
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

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))