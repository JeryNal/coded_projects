from flask import flask, redirect, url_for,render_template
app = flask(__name__)


@app.route("/")
def home():
    return "Hello!this is jerry main page"


@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


@app.route("/admin")
def admin():
    return redirect(url_for("home"))


if __name__ == "__main__":

    app.run()
