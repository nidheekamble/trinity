import os
from flask import Flask, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628cb0b12ce6c676dfde280ba246'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
Bootstrap(app)
datepicker(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from trinity import routes