from flask import render_template, request, redirect, url_for
from flask_login import login_user, current_user, logout_user
from auth import auth
from auth.models import Users

from app import db

from auth.forms import LoginForm, CreateAccountForm
from auth.util import verify_pass, hash_pass


@auth.route('/', methods=['GET', 'POST'])
@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if 'login' in request.form:

        # read form data
        # we can have here username OR email
        username = request.form['username']
        password = request.form['password']

        # Locate user
        user = Users.find_by_username(username)

        # if user not found
        if not user:

            user = Users.find_by_email(username)

            if not user:
                return render_template('auth/login.html', msg='Unknown User or Email', form=login_form)

        # Check the password
        if verify_pass(password, user.password):

            login_user(user)
            return redirect(url_for('auth.login'))

        # Something (user or pass) is not ok
        return render_template('auth/login.html',
                               msg='Wrong user or password',
                               form=login_form)

    if not current_user.is_authenticated:
        return render_template('auth/login.html',
                               form=login_form)
    return redirect(url_for('dashboard.home_page'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    create_account_form = CreateAccountForm(request.form)
    if 'register' in request.form:

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check username exists
        user = Users.query.filter_by(username=username).first()
        if user:
            return render_template('auth/register.html',
                                   msg='Username already registered',
                                   success=False,
                                   form=create_account_form)

        # Check email exists
        user = Users.query.filter_by(email=email).first()
        if user:
            return render_template('auth/register.html',
                                   msg='Email already registered',
                                   success=False,
                                   form=create_account_form)
        # else we can create the user
        user = Users(username=username, email=email, password=hash_pass(password))
        db.session.add(user)
        db.session.commit()

        # Delete user from session
        logout_user()

        return render_template('auth/register.html',
                               msg='User created successfully.',
                               success=True,
                               form=create_account_form)

    else:
        return render_template('auth/register.html', form=create_account_form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
