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
            db.session.add(user)
            db.session.commit()
        except Exception:
            return 'error'
        return redirect("/users")

@app.route("/users/assign", methods=['GET', 'POST'])
def assign_user():
    if request.method == 'GET':
        return render_template("assign_user.html")
    if request.method == 'POST':
        try:
            username = request.form['username']
            taskname = request.form['task']
            projectname = request.form['project']
            user = db.session.query(User).filter(User.username == username).first()
            task = db.session.query(Task).filter(Task.name == taskname).first()
            project = db.session.query(Project).filter(Project.name == projectname).first()
            user.tasks = task
            user.projects = project
            if task is not None and project is not None:
                task.projects = project
                db.session.add(task)
            db.session.add(user)
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
        return render_template("add_project.html")
    if request.method == 'POST':
        try:
            name = request.form['name']
            project = Project(name=name)
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

@app.route("/tasks/add", methods=['GET', 'POST'])
def add_task():
    if request.method == 'GET':
        return render_template("add_task.html")
    if request.method == 'POST':
        try:
            name = request.form['name']
            text = request.form['text']
            deadline = request.form['deadline']
            task = Task(name=name, text=text, deadline=deadline)
            db.session.add(task)
            db.session.commit()
        except Exception:
            return 'error'
        return redirect("/tasks")

@app.route("/tasks/assign", methods=['GET', 'POST'])
def assign_task():
    if request.method == 'GET':
        return render_template("assign_task.html")
    if request.method == 'POST':
        try:
            name = request.form['name']
            project = request.form['project']
            task = db.session.query(Task).filter(Task.name == name).first()
            project = db.session.query(Project).filter(Project.name == project).first()
            task.projects = project
            db.session.add(task)
            db.session.commit()
        except Exception:
            return 'error'
        return redirect("/tasks")
