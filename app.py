from flask import Flask, render_template

from blueprints.url_blueprint import url as url_blueprint

app = Flask(__name__, template_folder='static')


@app.route('/', methods=["GET"])
def index_handler():
    return render_template("index.html")


if __name__ == "__main__":
    app.register_blueprint(url_blueprint)

    app.run()
