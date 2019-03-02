from flask import jsonify

class Login_manager:
    @classmethod
    def valid_login(cls, username, password):
        if username == '' and password == '':
            return True
        else:
            return False


    @classmethod
    def login_success(cls):
        dic = {}
        dic['code'] = 200
        dic['message'] = 'login success'
        return jsonify(dic)


    @classmethod
    def login_failure(cls):
        dic = {}
        dic['code'] = 400
        dic['message'] = 'login failure'
        return jsonify(dic)



