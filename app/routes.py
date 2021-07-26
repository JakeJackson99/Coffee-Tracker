from flask import render_template
from flask_login import login_required

from app import app
from app.models import Bean


@app.route('/')
def index():
    beans = Bean.query.all()
    return render_template('index.html', beans=beans)


@app.route('/admin')
@login_required
def admin():
    pass
