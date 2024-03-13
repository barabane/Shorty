import os

from flask import Flask
from flask_login import LoginManager

from blueprints.auth_blueprint import auth as auth_blueprint
from blueprints.main_blueprint import main as main_blueprint
from blueprints.url_blueprint import url as url_blueprint
from db import db

app = Flask(__name__, template_folder='static')

login_manager = LoginManager()


@login_manager.user_loader
def user_loader_handler(user_id):
    return db.get_user_by_id(user_id=user_id)


if __name__ == "__main__":
    app.config['WTF_CSRF_SECRET_KEY '] = True
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    app.register_blueprint(url_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    login_manager.init_app(app=app)

    app.run()
