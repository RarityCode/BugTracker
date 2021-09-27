from __main__ import db


class Leader(db.Model):
    __tablename__ = 'leader'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    projects = db.relationship('Project', backref='leader', lazy=True)

    def __repr__(self):
        return f'{self.user}'


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    tasks = db.relationship('Task', backref='users', lazy=True)
    leader = db.relationship('Leader', backref='user', uselist=False, cascade='all, delete', lazy=True)

    def __repr__(self):
        return f'{self.username}'


class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    users = db.relationship('User', backref='projects', lazy=True)
    tasks = db.relationship('Task', backref='projects', cascade='all, delete', lazy=True)
    leader_id = db.Column(db.Integer, db.ForeignKey('leader.id'))

    def __repr__(self):
        return f'{self.name}'


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    text = db.Column(db.String(500), unique=False, nullable=False)
    deadline = db.Column(db.String(200), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))

    def __repr__(self):
        return f'{self.name}'
