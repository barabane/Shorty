from flask import Blueprint, redirect, url_for, render_template, flash
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from db import db
from forms.AuthForm import AuthForm

auth = Blueprint(name="auth", url_prefix="/auth/", import_name="auth")


@auth.route('/')
@auth.route('/signin', methods=["GET", "POST"])
def signin_handler():
    form = AuthForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = db.get_user_by_email(email=email)
        if not user:
            flash(message='Такого пользователя не существует', category='error')
            return render_template('auth.html', form=form)

        if not check_password_hash(pwhash=user.password, password=password):
            flash(message='Неправильный логин/пароль', category='error')
            return render_template('auth.html', form=form)
        login_user(user=user, remember=True)
        return redirect(url_for('main.index_handler'))
    return render_template('auth.html', form=form)


@auth.route('/')
@auth.route('/signup', methods=["GET", "POST"])
def signup_handler():
    form = AuthForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user_exists = db.get_user_by_email(email=email)
        if user_exists:
            flash(message='Такой пользователь уже существует', category='error')
            return render_template('auth.html', form=form)

        db.register_user(email=email, password=password)
        login_user(user=user_exists, remember=True)
        return redirect(url_for('main.index_handler'))
    return render_template('auth.html', form=form)


@auth.route('/logout')
def logout_handler():
    logout_user()
    return redirect(url_for('main.index_handler'))
