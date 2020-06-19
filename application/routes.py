from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, bcrypt, login_manager
from application.models import Admin, Contact, Locations
from application.forms import LoginForm, NewContactForm

from application import app 

@app.route('/')
def home():
    contacts = Contact.query.all()
    return render_template('home.html', contacts = contacts)

@app.route('/newcontact', methods=['GET', 'POST'])
def new():
    form = NewContactForm()
    cities = Locations.query.all()
    for city in cities:
        form.city.choices.append(str(city.city))

    if form.validate_on_submit() == False:
        print(form.errors)
    else:
        if isinstance(str(form.city.data), str):
            location = Locations.query.filter_by(form.city.data).first()
            Data = Contact(
                first_name = form.first_name.data,
                last_name = form.last_name.data, 
                email_address = form.email_address.data,
                phone_number = form.phone_number.data,
                location_id = str(form.city.data)
            )
            db.session.add(Data)
            db.session.commit()
            return redirect(url_for('home'))

    
    return render_template('new_contact.html', form=form)

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


