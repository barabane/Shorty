from flask import Flask, render_template

app = Flask(__name__, template_folder='static')


@app.route('/', methods=["GET"])
def index_handler():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
