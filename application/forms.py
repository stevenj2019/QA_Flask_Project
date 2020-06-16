from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
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
    
class RegisterForm(FlaskForm):
    first_name = StringField('First Name: ',
        validators=[
            DataRequired(),
            Length(min=3, max=10)
        ]
    )
    last_name = StringField('Last Name: ',
        validators=[
            DataRequired(),
            Length(min=5 ,max=15)
        ]
    )
    phone_number = StringField('Phone Numbers: ',
        validators=[
            DataRequired(),
            Email()
        ]
    )
    email = StringField('Email: ',
        validators=[
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField('Password: ',
        validators=[
            DataRequired()
        ] 
    )
    confirm_password = PasswordField('Confirm Password: ',
        validators=[
            DataRequired()
        ]
    )
    submit = SubmitField('Register!')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use')