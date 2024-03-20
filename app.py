import os

from flask import Flask, redirect, url_for, flash
from flask_login import LoginManager

from blueprints.auth_blueprint import auth as auth_blueprint
from blueprints.main_blueprint import main as main_blueprint
from blueprints.url_blueprint import url as url_blueprint
from converters.regexp_converter import RegexConverter
from db import db

app = Flask(__name__, template_folder='static')

login_manager = LoginManager()


@login_manager.user_loader
def user_loader_handler(user_id):
    return db.get_user_by_id(user_id=user_id)


@login_manager.unauthorized_handler
def unauthorized():
    flash('Для начала вам нужно авторизоваться', category='error')
    return redirect(url_for('main.index_handler'))


if __name__ == "__main__":
    app.config['WTF_CSRF_SECRET_KEY '] = True
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    app.url_map.converters['regex'] = RegexConverter
    app.register_blueprint(url_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    login_manager.init_app(app=app)

    app.run()
