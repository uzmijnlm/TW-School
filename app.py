#!/usr/bin/env python3

from . import app
from .models import User, Class, Problem, Item
from .login import Login_manager

import json
from flask import request
from flask import jsonify


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
        users_.append(user.id)

    return jsonify(users_)


@app.route('/classinfo')
def classinfo():
    #userid = request.cookie['userid']
    userid = 1
    currentclass = User.query.filter_by(id=userid).first().currentclass
    classinfo = Class.query.filter_by(id=currentclass).first().info
    return jsonify({'class_info': classinfo})


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




@app.route('/')
def index():
    return 'index page'
