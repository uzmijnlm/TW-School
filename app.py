#!/usr/bin/env python3

from . import app
from .models import User, Class

import json


@app.route('/users')
def users():
    users_ = []
    for user in User.query.all():
        users_.append(user.username)

    return json.dumps(users_)


@app.route('/class')
def getclass():
    class_ = []
    for c in Class.query.all():
        class_.append(c.info)
    return json.dumps(class_)


@app.route('/')
def index():
    return 'index page'
