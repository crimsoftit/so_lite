from functools import wraps
from flask import Flask, session, redirect, \
 url_for, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


# create the application object
app = Flask(__name__)
bcrypt = Bcrypt(app)

# config
import os
app.config.from_object(os.environ["APP_SETTINGS"])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create the sqlalchemy object
db = SQLAlchemy(app)

from models import *
from project.users.views import users_blueprint

# register blueprint
app.register_blueprint(users_blueprint)


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("login required")
            return redirect(url_for('users.login'))
    return wrap


@app.route('/')
def index():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
