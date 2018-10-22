from functools import wraps
from flask import Flask, session, redirect, \
 url_for, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
import os
# import sqlite3


# create the application object
app = Flask(__name__)

# config
app.config.from_object(os.environ["APP_SETTINGS"])

# create the sqlalchemy object
db = SQLAlchemy(app)

from models import *


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("login required")
            return redirect(url_for('login'))
    return wrap


@app.route('/')
def index():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", posts=posts)


@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'invalid credentials. please try again'
        else:
            session['logged_in'] = True
            flash('login successful')
            return redirect(url_for('index'))
    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    flash('you were logged out')
    return redirect(url_for("login"))


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")


@app.route("/profile")
@login_required
def profile():
    return render_template("u_account.html")


@app.route("/profile/my_recent_qstns")
@login_required
def my_recent_qstns():
    return render_template("my_recent_qstns.html")


@app.route("/profile/my_qstns")
@login_required
def my_qstns():
    return render_template("my_qstns.html")


@app.route("/profile/my_answers", methods=["GET"])
@login_required
def my_answers():
    return render_template("my_answers.html")



if __name__ == "__main__":
    app.run(debug=True)
