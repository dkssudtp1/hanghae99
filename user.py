from flask import jsonify, request
from db import db

#로그인
def sign_in():
    id_receive = request.form['id_give']
    password_receive = request.form['password_give']

    user = db.users.find_one({'id':id_receive})

    if user is None:
        return jsonify({'msg': '해당하는 아이디가 없습니다'})
    else :

        if user['password'] == password_receive :
            return jsonify({'user': ''})

        else :
            return jsonify({'msg': '비밀번호가 틀립니다'})

#회원가입
def sign_up():
    id_receive = request.form['id_give']
    password_receive = request.form['password_give']
    nickname_receive = request.form['nickname_give']

    user_list = list(db.users.find({}, {'_id': False}).sort('num'))

    last_user_num = user_list[-1]['num'] if len(user_list) > 0 else 1

    db.place.insert_one({"num": last_user_num + 1, "id": id_receive, "password": password_receive, "nickname": nickname_receive})

    return jsonify({'msg': '회원가입 완료'})

def user_get(token: str):
    return jsonify({'user': ''})
