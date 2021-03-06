from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Locations
from flask_login import current_user

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired()
        ]
    )
    password = PasswordField('Password', 
        validators=[
            DataRequired()
        ]
    )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

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
    city = SelectField('City',
        choices = [],
        coerce=int,
        validators=[
            DataRequired()
            ]
        )

    submit = SubmitField()

class EditContactForm(FlaskForm):

    email_address = StringField('Email Address', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    city = SelectField('City', choices= [], coerce=int, validators=[DataRequired()])
    submit=SubmitField()