from application import app
from flask import render_template, request


@app.route("/forum")
def forum():
    return render_template("forum.html")