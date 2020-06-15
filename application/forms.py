from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, PhoneNumberField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user

class Login_Form(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired()
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
    
class Register_Form(FlaskForm):
    first_name = StringField('First Name: ',
        validators=[
            DataRequired()
            Length=(min=3, max=10)
        ]
    )
    last_name = StringField('Last Name: ',
        validators=[
            DataRequired()
            Length=(mind=5 ,max=15)
        ]
    )
    Phone_number = PhoneNumberField('Phone Numbers: ',
        country_code='UK',
        display_format='national'
    )
    email = StringField('Email: ',
        validators=[
            DataRequired()
            Email()
        ]
    )
    password = PasswordField(
        validators=[
            DataRequired()
        ] 
    )
    confirm_password = PasswordField(
        validators=[
            DataRequired()
        ]
    )
    submit = SubmitField('Register!')