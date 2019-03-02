#!/usr/bin/env python3

from . import app
from .models import User
from .login import Login_manager

import json
from flask import request


@app.route('/login', methods=['GET'])
def login():
    error = None
    if request.method == 'POST':
        if Login_manager.valid_login(request.form['username'], request.form['password']):
            return Login_manager.login_success()
        else:
            error = 'Invalid username/password'
            return Login_manager.login_failure()
    return Login_manager.login_failure()


@app.route('/users')
def users():
    users_ = []
    for user in User.query.all():
        users_.append(user.username)

    return json.dumps(users_)


@app.route('/')
def index():
    return 'index page'
