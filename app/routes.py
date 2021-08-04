from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user, logout_user, login_user
from werkzeug.urls import url_parse

from app import app, db
from app.models import Bean, AdminUser
from app.forms import LoginForm, BeanForm


@app.route('/')
def index():
    beans = Bean.query.all()
    return render_template('index.html', beans=beans)


@app.route('/admin')
@login_required
def admin():
    beans = Bean.query.all()
    return render_template('admin.html', beans=beans)


@app.route('/add_bean', methods=['POST', 'GET'])
@login_required
def add_bean():
    form = BeanForm()
    if form.validate_on_submit():
        bean = Bean(name=form.name.data, country=form.country.data,
                    region=form.region.data,
                    description=form.description.data, rating=form.rating.data)
        db.session.add(bean)
        db.session.commit()
        flash('Successfully added a new bean')
        return redirect(url_for('admin'))
    return render_template('add_bean.html', title='Add New Bean', form=form)


@app.route('/edit_bean/<bean_id>', methods=['GET', 'POST'])
@login_required
def edit_bean(bean_id):
    form = BeanForm()
    bean = Bean.query.filter_by(id=bean_id).first()     # Might not first()'
    if form.validate_on_submit():
        bean.name = form.name.data
        bean.country = form.country.data
        bean.region = form.region.data
        bean.description = form.description.data
        bean.rating = form.rating.data
        db.session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('admin'))
    elif request.method == 'GET':
        form.name.data = bean.name
        form.country.data = bean.country
        form.region.data = bean.region
        form.description.data = bean.description
        form.rating.data = bean.rating
    return render_template('edit_bean.html', title='Edit Bean', form=form)


@app.route('/remove_bean/<bean_id>', methods=['GET'])
@login_required
def remove_bean(bean_id):
    Bean.query.filter_by(id=bean_id).delete()
    db.session.commit()
    return redirect(url_for('admin'))


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
