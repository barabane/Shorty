from flask import Blueprint, request, redirect, url_for, abort
from flask_login import current_user, login_required

from db import db

url = Blueprint(name="url", url_prefix="/url/", import_name="url")


@url.post('/create')
@login_required
def create_url_handler():
    db.create_url(full_url=request.form.get('url'), user_id=current_user.id)
    return redirect(url_for('main.index_handler'))


@url.get('/delete/<url_id>')
@login_required
def delete_url_handler(url_id: int):
    if db.get_user_url(current_user.id, url_id):
        db.delete_url(url_id=url_id)
        return redirect(url_for('main.index_handler'))
    return abort(403)
