import os

from flask import Flask, render_template

from blueprints.auth_blueprint import auth as auth_blueprint
from blueprints.main_blueprint import main as main_blueprint
from blueprints.url_blueprint import url as url_blueprint
from converters.regexp_converter import RegexConverter
from login_manager import login_manager

app = Flask(__name__, template_folder='static')

app.config['WTF_CSRF_SECRET_KEY '] = True
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.url_map.converters['regex'] = RegexConverter
app.register_blueprint(url_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)
login_manager.init_app(app=app)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run()
