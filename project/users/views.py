from functools import wraps
from flask import flash, redirect, render_template, request, \
    session, url_for, Blueprint


users_blueprint = Blueprint(
        'users', __name__,
        template_folder='templates'
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


@users_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'invalid credentials. please try again'
        else:
            session['logged_in'] = True
            flash('login successful')
            return redirect(url_for('home.index'))
    return render_template("login.html", error=error)


@users_blueprint.route("/logout")
def logout():
    session.pop('logged_in', None)
    flash('you were logged out')
    return redirect(url_for("users.login"))


@users_blueprint.route("/signup", methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")


@users_blueprint.route("/profile")
@login_required
def profile():
    return render_template("u_account.html")


@users_blueprint.route("/profile/my_recent_qstns")
@login_required
def my_recent_qstns():
    return render_template("my_recent_qstns.html")


@users_blueprint.route("/profile/my_qstns")
@login_required
def my_qstns():
    return render_template("my_qstns.html")


@users_blueprint.route("/profile/my_answers", methods=["GET"])
@login_required
def my_answers():
    return render_template("my_answers.html")
