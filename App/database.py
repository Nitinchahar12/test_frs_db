import pymongo
from pymongo import MongoClient

def mongo_collection():
    """ Creating database in mongodb """
    client = MongoClient('localhost', 27017)
    db = client.face_data
    collection = db.faces_captured
    return collection
