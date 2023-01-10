from flask import jsonify, request
from db import db



def my_place_list_get():
    category_num = request.args.get('category_num')
    user_num = request.args.get('user_num')

    my_place_list = db.place.aggregate([
        {
            '$lookup': {
                'from': "category",
                'localField': "category_num",
                'foreignField': "num",
                'as': "category",
            },
        },
        {
            '$lookup': {
                'from': "user",
                'localField': "user_num",
                'foreignField': "num",
                'as': "user",
            },
        },
        {
            '$match': {'category.num': int(category_num), 'user.num': int(user_num)}
        },
        {
            '$unset': ["_id", 'category_num', 'user_num', 'user._id', 'user.password','category._id']
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

    place_list = list(db.place.find({}, {'_id': False}))

    category = db.category.find_one({'num': int(category_num)}, {'_id': False})
    user = db.user.find_one({'num': int(user_num)}, {'_id': False})

    count = len(place_list)

    db.place.insert_one({"num": count + 1, "name": name, "content": content, 'img': img, 'category_num': category['num'], 'user_num': user['num'] })
    return jsonify({'msg': '등록 완료'})
