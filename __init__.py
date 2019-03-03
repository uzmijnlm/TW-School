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
    from .models import User, Class, Problem, Item, UserClassRelation
    u0 = User(username='u0', password='u0', currentclass=1)
    u1 = User(username='u1', password='u1', currentclass=1)
    u2 = User(username='u2', password='u2', currentclass=2)
    u3 = User(username='u3', password='u3', currentclass=2)
    u4 = User(username='u4', password='u4', currentclass=2)
    u5 = User(username='u5', password='u5', currentclass=1)
    c1 = Class(title='课程一 21天精通VUE', info='21天精通VUE, 愉快学习，轻松拿offer', learn_url='https://time.geekbang.org/')
    c2 = Class(title='课程二 21天精通FLASK', info='21天精通Flask, 愉快学习，轻松拿offer', learn_url='https://time.geekbang.org/')
    c3 = Class(title='课程三 21天精通Python', info='21天精通Python, 愉快学习，轻松拿offer', learn_url='https://time.geekbang.org/')
    c4 = Class(title='课程四 21天精通JAVA', info='21天精通JAVA, 愉快学习，轻松拿offer', learn_url='https://time.geekbang.org/')
    c5 = Class(title='课程五 21天精通Swift', info='Swift Go, 愉快学习，轻松拿offer', learn_url='https://time.geekbang.org/')
    c6 = Class(title='课程六 21天精通Sketch', info='Sketch大法好, 愉快学习，轻松拿offer', learn_url='https://time.geekbang.org/')
    p1 = Problem(content='which is right?', classId=1)
    p2 = Problem(content='which is right?', classId=1)
    i1 = Item(content='xxxxx', problemId=1, correct=0)
    i2 = Item(content='yyyyy', problemId=1, correct=1)
    i3 = Item(content='xxxxx', problemId=2, correct=0)
    i4 = Item(content='yyyyy', problemId=2, correct=1)
    i5 = Item(content='zzzzz', problemId=2, correct=0)
    uc0 = UserClassRelation(userId=1, classId=1)
    db.session.add_all([u0, u1, u2, u3, u4, u5, c1, c2, c3, c4, c5, c6, p1, p2, i1, i2, i3, i4, i5, uc0])
    db.session.commit()


init_app()
