from flask import jsonify, request
from db import db

def random_place_get():
    return jsonify({'place': ''})
