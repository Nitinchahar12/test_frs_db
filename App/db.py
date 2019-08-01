from pymongo import MongoClient
import string
import os
import hypothesis as h
import hypothesis.strategies as hs
from faker import Faker
from datetime import datetime
import os
from imutils import paths

def mongo_collection():
    client = MongoClient('localhost', 27017)
    db = client.face_data
    collection = db.faces_captured
    Entries = { "Name": Name[i] ,
            "DOB": fake.date(pattern="%Y-%m-%d"),
            "Phone": fake.phone_number() ,
            "Rank":fake.numerify(text="##") ,
            "service_number": fake.numerify(text="#########") ,
            "company": fake.company() ,
            "unit": fake.numerify(text="###"),
            "remarks": fake.lexify(text="???????????????", letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")  ,
            "Uploaded_Image": imagePaths[i] ,
            "is_suspicious": fake.boolean(chance_of_getting_true=50),

             }
