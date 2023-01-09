from flask import jsonify, request
from db import db

#
def sign_in():
    return jsonify({'user': ''})

def sign_up():
    return jsonify({'msg': '회원가입 완료'})

def user_get(token: str):
    return jsonify({'user': ''})
