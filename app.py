import os

from flask import Flask, render_template
from flask_login import LoginManager
from db import db

from blueprints.url_blueprint import url as url_blueprint

app = Flask(__name__, template_folder='static')
app.secret_key = os.getenv('SECRET_KEY')

login_manager = LoginManager()


@app.route('/', methods=["GET"])
def index_handler():
    return render_template("index.html")


@login_manager.user_loader
def user_loader_handler(user_id):
    return db.get_user_by_id(user_id=user_id)


if __name__ == "__main__":
    app.register_blueprint(url_blueprint)
    login_manager.init_app(app=app)

    app.run()
