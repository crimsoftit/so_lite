
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os


# create the application object
app = Flask(__name__)
bcrypt = Bcrypt(app)

# config
app.config.from_object(os.environ["APP_SETTINGS"])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create the sqlalchemy object
db = SQLAlchemy(app)

from project.users.views import users_blueprint
from project.home.views import home_blueprint

# register blueprint
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)
