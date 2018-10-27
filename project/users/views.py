from flask import flash, redirect, render_template, request, \
    session, url_for, Blueprint
from flask_login import login_user, login_required, logout_user
from .forms import LoginForm, RegForm
from project import db
from project.models import User, bcrypt


users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)


@users_blueprint.route("/signup", methods=['GET', 'POST'])
def signup():
    form = RegForm()
    if form.validate_on_submit():
        user = User(
            name=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        session["logged_in"] = True
        login_user(user)
        return redirect(url_for("home.index"))
    return render_template("signup.html", form=form)


@users_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
            if user is not None and bcrypt.check_password_hash(
                user.password, request.form['password']):
                session["logged_in"] = True
                login_user(user)
                flash("login successful!")
                return redirect(url_for(request.args.get('next', "home.index")))
            else:
                error = "invalid credentials. please try again!"
        else:
            error = "invalid credentials. please try again!"
    return render_template('login.html', form=form, error=error)


@users_blueprint.route("/logout")
def logout():
    logout_user()
    session.pop('logged_in', None)
    flash('you were logged out')
    return redirect(url_for("users.login"))


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
