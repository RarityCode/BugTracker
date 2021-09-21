from __main__ import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))

    def __repr__(self):
        return f'{self.username}'


class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    users = db.relationship('User', backref='projects', lazy=True)
    tasks = db.relationship('Task', backref='projects', cascade='all, delete', lazy=True)

    def __repr__(self):
        return f'{self.name}'


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    text = db.Column(db.String(500), unique=False, nullable=False)
    deadline = db.Column(db.String(200), unique=False, nullable=False)
    users = db.relationship('User', backref='tasks', lazy=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))

    def __repr__(self):
        return f'{self.name}'
