#!/usr/bin/env python3

from . import app
from .models import User, Class, Item, Problem
from .login import Login_manager
from flask import request
from flask import jsonify
from flask import make_response

@app.before_request
def check_cookie():
    cookie = request.cookies.get('cookie-user_id')
    if cookie is None and request.path != '/login':
        dic = {}
        dic['code'] = 401
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

@app.route('/exam')
def exam():
    user_id = 1
    current_class = User.query.filter_by(id=user_id).first().currentclass
    problem_list = []
    problems = Problem.query.filter_by(classId=current_class).all()
    selection = {'1': 'A', '2': 'B', '3': 'C', '4': 'D'}
    for no, problem in enumerate(problems):
        problem_dict = {}
        problem_no = no
        problem_id = problem.id
        content = problem.content
        item_list = []
        items = Item.query.filter_by(problemId=problem_id).all()
        for i, item in enumerate(items):
            item_dict = {}
            item_id = item.id
            item_content = item.content
            item_symbol = selection.get(str(i+1))
            item_dict['item_id'] = item_id
            item_dict['item_content'] = item_content
            item_dict['selection'] = item_symbol
            item_list.append(item_dict)
        problem_dict['no'] = problem_no
        problem_dict['problem_id'] = problem_id
        problem_dict['content'] = content
        problem_dict['items'] = item_list
        problem_list.append(problem_dict)
    return jsonify(problem_list)

@app.route('/class')
def get_class():
    class_all = Class.query.all()
    class_list = []
    for c in class_all:
        class_dic = {}
        class_dic['id'] = c.id
        class_dic['info'] = c.info
        class_dic['title'] = c.title
        class_dic['learn_url'] = c.learn_url
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
