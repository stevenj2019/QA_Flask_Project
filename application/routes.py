from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, bcrypt, login_manager
from application.models import Admin, Contact, Locations
from application.forms import LoginForm, NewContactForm, EditContactForm

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
        form.city.choices.append([city.location_id, city.city])
    if form.validate_on_submit():
        Data = Contact(first_name = form.first_name.data, last_name = form.last_name.data, email_address = form.email_address.data, phone_number = form.phone_number.data, location_id = form.city.data)
        db.session.add(Data)
        db.session.commit()

        return redirect(url_for('home'))
    else:
        print(form.city.data)
        print(form.errors)
    
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

@app.route('/update/<user_id>', methods=['GET', 'POST'])
def edit(user_id):
    form = EditContactForm(city=Contact.query.filter_by(contact_id=user_id).first().location_id)
    current_data = Contact.query.filter_by(contact_id=user_id).first()
    for city in Locations.query.all():
        form.city.choices.append([city.location_id, city.city])
    if form.validate_on_submit():
        current_data.email_address = form.email_address.data
        current_data.phone_number = form.phone_number.data
        current_data.location_id = form.city.data
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.email_address.data = current_data.email_address
        form.phone_number.data = current_data.phone_number
    return render_template('account.html', form=form, data=current_data)

@app.route('/delete/<user_id>')
def delete(user_id):
    db.session.delete(Contact.query.filter_by(contact_id=user_id).first())
    db.session.commit()
    return redirect(url_for('home'))