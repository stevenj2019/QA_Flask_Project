from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, bcrypt, login_manager
from application.models import Users, Office_Locations
from application.forms import Register_Form, Login_Form

from application import app 

@app.route('/', methods=['GET', 'POST'])
def auth():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form1 = Login_Form
    if form1.validate_on_sumbit():
        user = Users.query.filter_by(email=form1.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form1.password.data):
            login_user(user, form1.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))

    form2 = Register_Form
    if form2.validate_on_submit():
        user = Users(
            first_name = 
            last_name = 
            phone_number = 
            email = 
            password = bcrypt.generate_password_hash(form2.password.data)
            office_address = 
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth'))
    else:
        print(form.errors)

    render_template('auth.html', form1 = form_1, form2 = form_2)

@app.route('/home')
def home():
