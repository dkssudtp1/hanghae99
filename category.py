from flask import jsonify, request
from db import db



def category_list_get():
    #카테고리 가져오기
    category_List = list(db.category.find({}, {'_id': False}))

    ##정렬 반대로 하기
    category_List = list(reversed(category_List))

    return jsonify({'category_List': category_List})

def category_delete():

    return jsonify({'msg': '삭제 완료'})

def category_post():
    return jsonify({'msg': '등록 완료'})
