from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from flask_tutorial_blog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                           validators=[DataRequired(), Length(min=8, max=50)])
    confirm_password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=8, max=50), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose a different one.')

    def validate_email(self, email):

        user = User.query.filter_by(username=email.data).first()
        if user:
            raise ValidationError('E-mail already used. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                           validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    login = SubmitField('Login')
