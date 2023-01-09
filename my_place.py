from flask import jsonify, request
from db import db



def my_place_list_get_api():
    place_list = list(db.place.find({}, {'_id': False}))

    return jsonify({'place_list': place_list})

def my_place_delete():
    num_receive = request.form['num_give']

    db.place.delete_one({'num':num_recieve})

    return jsonify({'msg': '삭제 완료'})

def my_place_post():
    content_receive = request.form['content_give']
    title_receive = request.form['title_give']
    img_receive = request.form['img_give']

    place_list = list(db.place.find({}, {'_id': False}))
    count = len(place_list) + 1

    doc = {
        'num': count,
        'title': title_receive,
        'content': content_receive,
        'img': img_receive
    }

    db.place.insert_one(doc)

    return jsonify({'msg': '등록 완료'})
