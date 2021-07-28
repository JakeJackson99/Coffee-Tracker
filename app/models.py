from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db, login


@login.user_loader
def load_user(user_id):
    return AdminUser.query.get(user_id)


class Bean(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, nullable=False)
    country = db.Column(db.String(20), index=True)
    region = db.Column(db.String(20), index=True)
    description = db.Column(db.String(80))
    rating = db.Column(db.Integer, index=True, nullable=False)


class AdminUser(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, nullable=False, unique=True)
    password_hash = db.Column(db.String(200), unique=True)

    def __repr__(self):
        return '<Admin User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
