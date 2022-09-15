from pymongo import MongoClient

client = MongoClient("mongodb+srv://ineslahbib:R3KlRsefCslz0iEx@cluster0.qql3fuv.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_application

collection_name = db["todos_app"]