from pymongo import MongoClient

client = MongoClient(
        "mongodb+srv://test:sparta@cluster0.zphghpj.mongodb.net/?retryWrites=true&w=majority")
db = client.recommendplace