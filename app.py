#!/usr/bin/env python3

from . import app
from .models import User, Class
from .login import Login_manager
from flask import request
from flask import jsonify
from flask import make_response

@app.before_request
def check_cookie():
    cookie = request.cookies.get('cookie-user_id')
    if cookie is None and request.path != '/login':
        dic = {}
        dic['code'] = 400
        dic['message'] = 'please re-login'
        return jsonify(dic)

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user_id = Login_manager.valid_login(request.json['username'], request.json['password'])
        if user_id is not None:
            return Login_manager.login_success(user_id)
        else:
            return Login_manager.login_failure()
    return Login_manager.login_failure()

@app.route('/logout', methods=['GET'])
def logout():
    res = make_response('')
    res.delete_cookie('cookie-user_id')
    return res

@app.route('/users')
def users():
    users_ = []
    for user in User.query.all():
        users_.append(user.username)

    return jsonify(users_)


@app.route('/class')
def get_class():
    class_all = Class.query.all()
    class_list = []
    for c in class_all:
        class_dic = {}
        class_dic['info'] = c.info
        class_dic['title'] = c.title
        class_list.append(class_dic)

    dic = {}
    if class_list is not None:
        dic['code'] = 200
        dic['message'] = 'success'
        dic['classes'] = class_list
        return jsonify(dic)
    else:
        dic['code'] = 400
        dic['message'] = 'no classes'
        dic['classes'] = []
        return jsonify(dic)


@app.route('/')
def index():
    return 'index page'
