import random
from flask import jsonify, request
from db import db

def random_place_get():
    ##카테고리 중복값 없이 가져오기
    category_List = list(db.category.find({}, {'_id': False}))
    print(category_List)
    ##정렬 반대로 하기
    category_List = list(reversed(category_List))

    return jsonify({'category_List': category_List})

def random_place_post():
    """
    #음식 넘버 정하기
    korea_foods = 1
    china_foods = 2
    japan_foods = 3

    #클라이언트의 카테고리값 가져오기
    category_receive = int(request.form['category_give'])

    #카테고리값에 조건 붙이기
    if category_receive == korea_foods:
        foodList = list(db.foods.find({"category":"한식"}, {'_id': False}))
        print("한식")
    elif category_receive == china_foods:
        foodList = list(db.foods.find({"category":"중식"}, {'_id': False}))
        print("중식")
    elif category_receive == japan_foods:
        foodList = list(db.foods.find({"category":"일식"}, {'_id': False}))
        print("일식")
    else:
        foodList = list(db.foods.find({}, {'_id': False}))
    """

    # #클라이언트의 카테고리값 가져오기
    category_receive = int(request.form['category_give'])

    # 카테고리가 전체인지 아닌지 확인
    if category_receive == 0:
        foodList = list(db.place.find({}, {'_id': False}))
    else:
        foodList = list(db.place.find({"category_num": category_receive}, {'_id': False}))

    # 랜덤으로 리스트 중에서 선택
    random_food = random.choice(foodList)

    return jsonify({'food': random_food})