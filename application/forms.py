from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Locations
from flask_login import current_user

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField('Password', 
        validators=[
            DataRequired()
        ]
    )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use')

class NewContactForm(FlaskForm):
    first_name = StringField('First Name',
        validators=[
            DataRequired()
        ]
    )
    last_name = StringField('Last Name',
        validators=[
            DataRequired()
        ]
    )
    email_address = StringField('Email Address',
    validators=[
        DataRequired(),
        Email()
        ]
    )
    phone_number = StringField('Phone Number', 
        validators=[
            DataRequired()
        ]
    )
    cities = Locations.query.all().city
    city = SelectField('City',
        validators=[
            DataRequired()
            ]
        )

    submit = SubmitField()

class EditContactForm(FlaskForm):
    