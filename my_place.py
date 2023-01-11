from flask import jsonify, request
from db import db


def my_place_list_get():
    user_num = request.args.get('user_num')

    my_place_list = db.place.find({'user_num': int(user_num)}, {'_id': False})

    # my_place_list = db.place.aggregate([
    #     {
    #         # sql의 join기능을 수행
    #         '$lookup': {
    #             'from': "user",
    #             'localField': "user.num",
    #             'foreignField': "place.user_num",
    #             'as': "user",
    #         },
    #     },
    #     {
    #         # array -> object map으로 변환시켜준다
    #         '$unwind': {'path':'$user'}
    #     },
    #     {
    #         # 요청한 user의 번호를 기준삼아 진행한다
    #         '$match': {'user.num': int(user_num)}
    #     },
    #     {
    #         # 노출시키지 않을 컬럼을 제거시켜준다
    #         '$unset': ["_id", 'user_num', 'user._id', 'user.password']
    #     },
    # ])
    #
    json = jsonify({'place_list': list(my_place_list)})

    return json


def my_place_delete():
    num = request.form['num']

    try:
        db.place.delete_one({"num": int(num)})
        return "ok"
    except:
        return "error"


def my_place_post():

    try:
        content = request.form['content']
        title = request.form['title']
        img = request.form['img']
        category_num = request.form['category_num']
        user_num = request.form['user_num']

        # 장소목록을 num순으로 정렬
        place_list = list(db.place.find({}, {'_id': False}).sort('num'))

        # 마지막 번호를 호출한다
        last_palce_num = place_list[-1]['num'] if len(place_list) > 0 else 1

        category = db.category.find_one({'num': int(category_num)}, {'_id': False})
        user = db.users.find_one({'num': int(user_num)}, {'_id': False})

        db.place.insert_one(
            {"num": last_palce_num + 1, "title": title, "content": content, 'img': img, 'category_num': int(category['num']),
             'user_num': int(user['num'])})
        return 'ok'
    except:
        return 'fail'
