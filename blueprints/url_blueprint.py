from flask import Blueprint, request

url = Blueprint(name="url", url_prefix="/url/", import_name="url")


@url.route('/create', methods=["POST"])
def create_url_handler():
    print(request.form.get('url'))
    return 'hi'
