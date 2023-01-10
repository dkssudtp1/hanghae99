from flask import jsonify, request
from db import db



def my_place_list_get():
    user_num = request.form('user_num')

    my_place_list = db.place.aggregate([
        {
            '$lookup': {
                'from': "user",
                'localField': "user_num",
                'foreignField': "num",
                'as': "user",
            },
        },
        {
            '$match': {'user.num': int(user_num)}
        },
        {
            '$unset': ["_id", 'user_num', 'user._id', 'user.password']
        }
    ])

    json = jsonify({'place_list': list(my_place_list)})

    return json

def my_place_delete():
    num = request.args.get('num')

    db.place.delete_one({'num':int(num)})

    return jsonify({'msg': '삭제 완료'})

def my_place_post():

    content = request.form['content']
    name = request.form['name']
    img = request.form['img']
    category_num = request.form['category_num']
    user_num = request.form['user_num']

    place_list = list(db.place.find({}, {'_id': False}).sort('num'))

    last_palce_num = place_list[-1]['num'] if len(place_list) > 0 else 1

    category = db.category.find_one({'num': int(category_num)}, {'_id': False})
    user = db.user.find_one({'num': int(user_num)}, {'_id': False})

    db.place.insert_one({"num": last_palce_num + 1, "name": name, "content": content, 'img': img, 'category_num': category['num'], 'user_num': user['num'] })
    return jsonify({'msg': '등록 완료'})
