from flask_tutorial_blog.secret_settings import flask_secret_key


class Config:
    SECRET_KEY = flask_secret_key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'