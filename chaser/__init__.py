from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from settings.settings import io

from controller import MotorController

app = Flask(__name__, static_folder='static', static_url_path='')

app.config.from_object('settings.settings')
app.secret_key = app.config['SECRET_KEY']
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

motor_controller = MotorController()
from chaser import views, models
