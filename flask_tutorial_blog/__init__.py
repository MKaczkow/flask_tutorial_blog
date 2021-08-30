from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_tutorial_blog.secret_settings import flask_secret_key


app = Flask(__name__)
app.config['SECRET_KEY'] = flask_secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from flask_tutorial_blog import routes
