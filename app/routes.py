from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user, logout_user, login_user
from werkzeug.urls import url_parse

from app import app
from app.models import Bean, AdminUser
from app.forms import LoginForm


@app.route('/')
def index():
    beans = Bean.query.all()
    return render_template('index.html', beans=beans)


@app.route('/admin')
@login_required
def admin():
    beans = Bean.query.all()
    return render_template('admin.html', beans=beans)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = AdminUser.query.filter_by(name=form.name.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid name or password')
            return redirect(url_for('login'))

        login_user(user)

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('admin')
        return redirect(next_page)
        
    return render_template('login.html', title='Sign In', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
