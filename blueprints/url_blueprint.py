from flask import Blueprint, request, redirect, url_for
from flask_login import current_user, login_required

from db import db

url = Blueprint(name="url", url_prefix="/url/", import_name="url")


@url.route('/create', methods=["POST"])
@login_required
def create_url_handler():
    db.create_url(full_url=request.form.get('url'), user_id=current_user.id)
    return redirect(url_for('main.index_handler'))
