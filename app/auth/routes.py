from flask import render_template
from auth import auth


@auth.route('/')
@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/signup')
def signup():
    return render_template('auth/signup.html')


@auth.route('/logout')
def logout():
    return 'Logout'



