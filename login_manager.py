from flask import flash, redirect, url_for
from flask_login import LoginManager
from db import db

login_manager = LoginManager()


@login_manager.user_loader
def user_loader_handler(user_id):
    return db.get_user_by_id(user_id=user_id)


@login_manager.unauthorized_handler
def unauthorized():
    flash('Для начала вам нужно авторизоваться', category='error')
    return redirect(url_for('main.index_handler'))
