from database import mongo_collection
from imutils import paths
import os
import hypothesis as h
import hypothesis.strategies as hs
from faker import Faker




def mongo_data():
    number = int(input("Enter the number: "))
    imagePaths = list(paths.list_images("images"))
    l = os.listdir(path='images')
    Name=[x.split('.')[0] for x in l]
    fake = Faker()
    for i in range(number):
        entries = { "Name": Name[i] ,
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
        post_id = mongo_collection().insert_one(entries)

    return "Done"
