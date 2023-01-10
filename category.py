from flask import jsonify, request
from db import db



def category_list_get():

    return jsonify({'category_list': ''})

def category_delete():

    return jsonify({'msg': '삭제 완료'})

def category_post():
    return jsonify({'msg': '등록 완료'})
