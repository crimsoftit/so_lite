from functools import wraps
from flask import Flask, session, redirect, \
 url_for, request, render_template, flash, g
import sqlite3


app = Flask(__name__)

app.secret_key = 'yule_mguyz'
app.database = "sample.db"


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
    g.db = connect_db()
    cur = g.db.execute("SELECT * from posts")
    posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    g.db.close()
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


def connect_db():
    return sqlite3.connect(app.database)


if __name__ == "__main__":
    app.run(debug=True)
