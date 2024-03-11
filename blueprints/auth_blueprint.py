from flask import Blueprint, redirect, url_for, render_template, flash
from werkzeug.security import check_password_hash

from db import db
from forms.AuthForm import AuthForm

auth = Blueprint(name="auth", url_prefix="/auth/", import_name="auth")


@auth.route('/signin', methods=["GET", "POST"])
def signin_handler():
    form = AuthForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = db.get_user_by_email(email=email)
        if not user:
            flash(message='Такого пользователя не существует', category='error')
            return redirect(url_for('index_handler'))

        if not check_password_hash(pwhash=user.password, password=password):
            flash(message='Неправильный пароль', category='error')
            return redirect(url_for('index_handler'))
        return redirect(url_for('index_handler'))
    return render_template('index.html', form=form)


@auth.route('/signup', methods=["GET", "POST"])
def signup_handler():
    form = AuthForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user_exists = db.get_user_by_email(email=email)
        if user_exists:
            flash(message='Такой пользователь уже существует', category='error')
            return redirect(url_for('index_handler'))

        db.register_user(email=email, password=password)
        return redirect(url_for('index_handler'))
    return render_template('index.html', form=form)
