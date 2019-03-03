#!/usr/bin/env python3

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

DB_PATH = '/tmp/app.db'

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


# noinspection PyUnresolvedReferences
def init_app():
    try:
        os.remove('/tmp/app.db')
    except OSError:
        pass

    from .models import User
    db.create_all()
    preload_users()


def preload_users():
    from .models import User, Class, Problem, Item
    u0 = User(username='u0', password='u0', currentclass=1)
    u1 = User(username='u1', password='u1')
    u2 = User(username='u2', password='u2')
    u3 = User(username='u3', password='u3')
    u4 = User(username='u4', password='u4')
    u5 = User(username='u5', password='u5')
    c1 = Class(title='课程一 21天精通VUE', info='material of c1', learn_url='http://www.google.com')
    c2 = Class(title='课程二 21天精通FLASK', info='material of c2', learn_url='http://www.google.com')
    p1 = Problem(content='which is right?', classId=1)
    p2 = Problem(content='which is right?', classId=1)
    i1 = Item(content='xxxxx', problemId=1, correct=0)
    i2 = Item(content='yyyyy', problemId=1, correct=1)
    i3 = Item(content='xxxxx', problemId=2, correct=0)
    i4 = Item(content='yyyyy', problemId=2, correct=1)
    i5 = Item(content='zzzzz', problemId=2, correct=0)
    db.session.add_all([u0, u1, u2, u3, u4, u5, c1, c2, p1, p2, i1, i2, i3, i4, i5])
    db.session.commit()


init_app()
