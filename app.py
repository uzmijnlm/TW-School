#!/usr/bin/env python3

from . import app
from .models import Class
from .models import User
from .login import Login_manager
from flask import request
from flask import jsonify

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user_id = Login_manager.valid_login(request.json['username'], request.json['password'])
        if user_id is not None:
            return Login_manager.login_success()
        else:
            return Login_manager.login_failure()
    return Login_manager.login_failure()

@app.route('/users')
def users():
    users_ = []
    for user in User.query.all():
        users_.append(user.username)

    return jsonify(users_)


@app.route('/class')
def getclass():
    class_ = []
    for c in Class.query.all():
        class_.append(c.info)
    return jsonify(class_)


@app.route('/')
def index():
    return 'index page'
