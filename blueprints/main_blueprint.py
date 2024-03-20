from flask import Blueprint, render_template, redirect, request
from flask_login import current_user

from db import db

main = Blueprint(name="main", import_name='main')


@main.route('/', methods=["GET"])
def index_handler():
    urls = []
    if current_user.is_authenticated:
        urls = db.get_user_urls(user_id=current_user.id)
    return render_template("index.html", urls=urls)


@main.route("/<regex('^fp.+'):url_id>")
def url_handler(url_id):
    url = db.get_url_by_path(short_path='http://127.0.0.1:5000/' + url_id)
    db.add_visit(url_id=url.id, visit_ip=request.remote_addr)

    return redirect(url.full_path)
