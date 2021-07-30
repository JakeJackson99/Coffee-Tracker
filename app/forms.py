from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class BeanForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    country = StringField('Country')
    region = StringField('Region')
    description = StringField('Description', validators=[
                              Length(min=0, max=80)])
    rating = IntegerField('Rating', validators=[DataRequired()])
    submit = SubmitField('Add')