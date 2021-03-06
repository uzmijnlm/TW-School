from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    currentclass = db.Column(db.Integer, nullable=False, default=-1)

    def __repr__(self):
        return '<User %r>' % self.username


class UserClassRelation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, nullable=False)
    classId = db.Column(db.Integer, nullable=False)
    point = db.Column(db.Integer, nullable=True, default=-1)


class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    learn_url = db.Column(db.String, nullable=False)
    info = db.Column(db.String, nullable=True)


class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    classId = db.Column(db.Integer, nullable=False)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    problemId = db.Column(db.Integer, nullable=False)
    correct = db.Column(db.Integer, nullable=False)
