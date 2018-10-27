from project import app, db
from project.models import BlogPost
from functools import wraps
from flask import session, redirect, url_for, render_template, flash, Blueprint
from flask_login import login_required


# config
home_blueprint = Blueprint(
        'home', __name__,
        template_folder="templates"
    )


# routes
@home_blueprint.route('/')
def index():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", posts=posts)
