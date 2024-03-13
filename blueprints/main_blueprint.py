from flask import Blueprint, render_template
from flask_login import current_user

from db import db

main = Blueprint(name="main", import_name='main')


@main.route('/', methods=["GET"])
def index_handler():
    urls = []
    if current_user.is_authenticated:
        urls = db.get_user_urls(user_id=current_user.id)
    return render_template("index.html", urls=urls)
