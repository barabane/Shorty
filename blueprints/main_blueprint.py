from flask import Blueprint, render_template

main = Blueprint(name="main", import_name='main')


@main.route('/', methods=["GET"])
def index_handler():
    return render_template("index.html")
