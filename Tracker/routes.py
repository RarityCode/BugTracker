from flask import request, render_template, make_response, redirect
from flask import current_app as app
from .model import *


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users", methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return render_template("users.html", users=User.query.all())
    if request.method == 'POST':
        name = request.form['name']
        user = db.session.query(User).filter(User.username == name).first()
        db.session.delete(user)
        db.session.commit()
        return redirect("/users")

@app.route("/users/add", methods=['GET', 'POST'])
def add_user():
    if request.method == 'GET':
        return render_template("add_user.html")
    if request.method == 'POST':
        try:
            username = request.form['username']
            user = User(username=username)
            lead = Leader()
            user.leader = lead
            db.session.add(lead)
            db.session.add(user)
            db.session.commit()
        except Exception:
            return 'error'
        return redirect("/users")

@app.route("/users/assign", methods=['GET', 'POST'])
def assign_user():
    if request.method == 'GET':
        return render_template("assign_user.html",users = User.query.all(), projects=Project.query.all(), tasks=Task.query.all())
    if request.method == 'POST':
        try:
            user = request.form['user']
            task = request.form['task']
            user = db.session.query(User).filter(User.username == user).first()
            task = db.session.query(Task).filter(Task.name == task).first()
            task.users = user
            user.projects = task.projects
            db.session.add(task)
            db.session.commit()
        except Exception:
            return 'error'
        return redirect("/users")

@app.route("/projects", methods=['GET', 'POST'])
def projects():
    if request.method == 'GET':
        return render_template("projects.html", projects=Project.query.all())
    if request.method == 'POST':
        name = request.form['name']
        project = db.session.query(Project).filter(Project.name == name).first()
        db.session.delete(project)
        db.session.commit()
        return redirect("/projects")

@app.route("/projects/add", methods=['GET', 'POST'])
def add_project():
    if request.method == 'GET':
        return render_template("add_project.html",users = User.query.all())
    if request.method == 'POST':
        try:
            name = request.form['name']
            lead = request.form['username']
            project = Project(name=name)
            leader = db.session.query(Leader).filter(Leader.user.has(User.username == lead)).first()
            project.leader = leader
            db.session.add(project)
            db.session.commit()
        except Exception:
            return 'error'
        return redirect("/projects")

@app.route("/projects/assign", methods=['GET', 'POST'])
def assign_project():
    if request.method == 'GET':
        return render_template("assign_project.html",users = User.query.all(), projects=Project.query.all())
    if request.method == 'POST':
        try:
            project = request.form['project']
            leader = request.form['leader']
            project = db.session.query(Project).filter(Project.name == project).first()
            leader = db.session.query(Leader).filter(Leader.user.has(User.username == leader)).first()
            project.leader = leader
            db.session.add(project)
            db.session.commit()
        except Exception:
            return 'error'
        return redirect("/projects")

@app.route("/tasks", methods=['GET', 'POST'])
def tasks():
    if request.method == 'GET':
        return render_template("tasks.html", tasks=Task.query.all())
    if request.method == 'POST':
        name = request.form['name']
        task = db.session.query(Task).filter(Task.name == name).first()
        db.session.delete(task)
        db.session.commit()
        return redirect("/tasks")

@app.route("/tasks/<name>", methods=['GET'])
def task(name=None):
    task = Task.query.filter(Task.name == name).first()
    return render_template("task.html", task=task)

@app.route("/tasks/add", methods=['GET', 'POST'])
def add_task():
    if request.method == 'GET':
        return render_template("add_task.html", projects=Project.query.all(), users = User.query.all())
    if request.method == 'POST':
        try:
            name = request.form['name']
            text = request.form['text']
            deadline = request.form['deadline']
            project = request.form['project']
            user = request.form['user']
            task = Task(name=name, text=text, deadline=deadline)
            project = db.session.query(Project).filter(Project.name == project).first()
            user = db.session.query(User).filter(User.username == user).first()
            task.projects = project
            task.users = user
            user.projects = task.projects
            db.session.add(user)
            db.session.add(task)
            db.session.commit()
        except Exception:
            return 'error'
        return redirect("/tasks")

@app.route("/tasks/assign", methods=['GET', 'POST'])
def assign_task():
    if request.method == 'GET':
        return render_template("assign_task.html", projects=Project.query.all(), tasks=Task.query.all(), users = User.query.all())
    if request.method == 'POST':
        try:
            task = request.form['task']
            user = request.form['user']
            task = db.session.query(Task).filter(Task.name == task).first()
            user = db.session.query(User).filter(User.username == user).first()
            task.users = user
            user.projects = task.projects
            db.session.add(user)
            db.session.add(task)
            db.session.commit()
        except Exception:
            return 'error'
        return redirect("/tasks")
