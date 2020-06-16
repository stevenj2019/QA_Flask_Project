from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, bcrypt, login_manager
from application.models import Admin, Contact, Office_Locations
from application.forms import LoginForm

from application import app 

@app.route('/adminlogin', methods=['GET', 'POST'])
def auth():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, form.remember.data)
            return redirect(url_for('home'))
    else:
        print(form.errors)
    return render_template('auth.html', form = form)

#@app.route('/')
#def home():
