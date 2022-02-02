from flask import Blueprint, redirect, render_template, request, url_for
from .forms import LoginForm, UserInfoForm
from cozy_corner.models import User
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user
from cozy_corner import db, site

auth = Blueprint('auth', __name__, template_folder = 'user_auth_templates')

@auth.route('/')
def home():
    return render_template('index.html', title='Home')

@auth.route('/signin', methods=["GET","POST"])
def signIn():
    login_form = LoginForm()
    if request.method == "POST" and login_form.validate():
        username = login_form.username.data
        password = login_form.password.data
        remember_me = login_form.remember_me.data

        # check if user exists .first() == the first element of that list query
        user = User.query.filter_by(username=username).first()

        if user is None or not check_password_hash(user.password, password):
            print("wrong password")
            return render_template('signin.html', form = login_form)

        # log me in
        login_user(user, remember=remember_me)
        return redirect(url_for("site.profile"))

    return render_template('signin.html', form = login_form)
        

@auth.route('/signup', methods =["GET", "POST"])
def signUp():
    signup_form = UserInfoForm()
    if request.method == "POST":
        if signup_form.validate():
            print('form was validated')
            username = signup_form.username.data
            email = signup_form.email.data
            password = signup_form.password.data

            # create instance of new users
            user = User(username, email, password)
            # add instance of database 
            db.session.add(user)
            # commit to database like github
            db.session.commit()
        
            return redirect(url_for('home'))
        else: 
            print("not validated")

    return render_template('signup.html', form = signup_form)


@auth.route('/logout')
def logMeOut():
    logout_user()
    return redirect(url_for('auth.signIN'))
