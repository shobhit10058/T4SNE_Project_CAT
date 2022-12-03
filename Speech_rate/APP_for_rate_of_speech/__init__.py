from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from kombu.utils.url import safequote


application = Flask(__name__)

from APP_for_rate_of_speech import routes