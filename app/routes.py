from flask import render_template
from flask_login import current_user, login_user, login_required

from app import app
from app.models import AdminUser, Bean


@app.route('/')
def index():
    return render_template('index.html', beans=beans)

