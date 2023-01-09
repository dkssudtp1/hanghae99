from flask import jsonify, request
from db import db



def my_place_list_get():
    return jsonify({'place_list': ''})

def my_place_delete():
    return jsonify({'msg': '삭제 완료'})

def my_place_post():
    return jsonify({'msg': '등록 완료'})
