import random
from flask import jsonify, request
from db import db

def random_place_post():
    # #클라이언트의 카테고리값 가져오기
    category_receive = int(request.form['category_give'])

    # 카테고리가 전체인지 아닌지 확인
    if category_receive == 0:
        foodList = list(db.place.find({}, {'_id': False}))
    else:
        foodList = list(db.place.find({"category_num": category_receive}, {'_id': False}))

    if foodList == []:
        return "null"

    # 랜덤으로 리스트 중에서 선택
    random_food = random.choice(foodList)

    return jsonify({'food': random_food})