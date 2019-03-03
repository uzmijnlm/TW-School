from flask import jsonify
from .models import User

class Login_manager:
    @classmethod
    def valid_login(cls, username, password):
        user = cls.find_user(username)
        if user:
            if username == user.username and password == user.password:
                return user.id
            else:
                return None

    @classmethod
    def login_success(cls, user_id):
        dic = {}
        dic['code'] = 200
        dic['message'] = 'login success'
        import time
        res = jsonify(dic)
        res.set_cookie('cookie-user_id', str(user_id), expires=(time.time() + 300000))
        return res


    @classmethod
    def login_failure(cls):
        dic = {}
        dic['code'] = 400
        dic['message'] = 'login failure'
        return jsonify(dic)

    @classmethod
    def find_user(cls, username):
        return User.query.filter(User.username == username).first()
