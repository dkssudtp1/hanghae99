from flask import jsonify, request
from db import db

#로그인
def sign_in():
    id_receive = request.form['id_give']
    password_receive = request.form['password_give']

    user = db.users.find_one({'id':id_receive}, {'_id': False})

    if user is None:
        return "error"
    else :
        if user['password'] == password_receive :
            return jsonify({'user': user})

        else :
            return "error"

#회원가입
def sign_up():
    id_receive = request.form['id_give']
    password_receive = request.form['password_give']
    nickname_receive = request.form['nickname_give']

    existing_id = db.users.find_one({'id': id_receive})

    if existing_id is not None:
        return "error"
    else:

        user_list = list(db.users.find({}, {'_id': False}).sort('num'))

        last_user_num = user_list[-1]['num'] if len(user_list) > 0 else 1

        db.users.insert_one({"num": last_user_num + 1, "id": id_receive, "password": password_receive, "nickname": nickname_receive, "admin": False})

        return jsonify({'msg': '회원가입 완료'})

def user_get(token: str):
    return jsonify({'user': ''})
