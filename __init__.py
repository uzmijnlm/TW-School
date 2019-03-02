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
    from .models import User
    u0 = User(username='u0', password='u0')
    u1 = User(username='u1', password='u1')
    u2 = User(username='u2', password='u2')
    u3 = User(username='u3', password='u3')
    u4 = User(username='u4', password='u4')
    u5 = User(username='u5', password='u5')
    db.session.add_all([u0, u1, u2, u3, u4, u5])
    db.session.commit()


init_app()
