from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["username"] != "admin" or request.form["password"] != "admin":
            error = 'invalid credentials. please try again'
        else:
            return redirect(url_for("index"))
    return render_template("login.html", error=error)


if __name__ == "__main__":
    app.run(debug=True)
