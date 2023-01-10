import random
from flask import jsonify, request
from db import db


def place_list_get():
    category_num = int(request.args.get('category_num'))

    if category_num == 0:
        place_list = list(db.place.find({}, {'_id': False}))
        return jsonify({'place_list': list(place_list)})
    else:
        place_list = list(db.place.find({'category_num': category_num}, {'_id': False}))

        random.shuffle(place_list)

        return jsonify({'place_list': list(place_list)})

