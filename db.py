from pymongo import MongoClient

client = MongoClient("your DB")
db = client.recommendplace