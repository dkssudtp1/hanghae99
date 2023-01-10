from flask import jsonify, request
from db import db



def category_list_get():
    return jsonify({'category_List': category_select()})

def category_post():

    category_id = category_max_num() + 1
    category_receive = request.form['category_name']

    if category_duple_check(category_receive):
        return "duple"

    category = {
        'num': int(category_id),
        'name': str(category_receive),
    }

    return category_insert(category)

def category_put():

    num_receive = request.form['category_num']
    name_receive = request.form['category_name']

    if category_duple_check(name_receive):
        return "duple"

    category = {
        'modify_num': int(num_receive),
        'modify_name': str(name_receive),
    }

    return category_update(category)


def category_update(category):
    try:
        db.category.update_one({"num":category['modify_num']},{"$set":{"name":category['modify_name']}})
        return "ok"
    except:
        return "error"

def category_insert(category):
    try:
        db.category.insert_one(category)
        return "ok"
    except:
        return "error"

def category_delete():
    num_receive = int(request.form['category_num'])

    try:
        db.category.delete_one({"num":num_receive})
        return "ok"
    except:
        return "error"

def category_select():
    #카테고리 가져오기
    category_List = list(db.category.find({}, {'_id': False}))

    #정렬 반대로 하기
    category_List = list(reversed(category_List))

    return category_List

def category_max_num():

    #카테고리 내림차순으로 정렬 후 하나 가져오기
    max_num_list = list(db.category.find({}, {'_id': False}).sort("num",-1).limit(1))

    return int(max_num_list[0]['num'])

def category_duple_check(input_category):

    category_list = category_select()

    for category in category_list:
        if input_category == category['name']:
            return True






