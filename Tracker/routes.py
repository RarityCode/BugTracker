from flask import request, render_template, make_response
from flask import current_app as app
from .model import *


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users")
def users():
    return render_template("users.html", users=User.query.all())

@app.route("/projects")
def projects():
    return render_template("projects.html", projects=Project.query.all())

@app.route("/tasks")
def tasks():
    return render_template("tasks.html", tasks=Task.query.all())
