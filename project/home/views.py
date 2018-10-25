from project import app, db
from project.models import BlogPost
from functools import wraps
from flask import session, redirect, url_for, render_template, flash, Blueprint


# config
home_blueprint = Blueprint(
        'home', __name__,
        template_folder="templates"
    )


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


@home_blueprint.route('/')
def index():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", posts=posts)
