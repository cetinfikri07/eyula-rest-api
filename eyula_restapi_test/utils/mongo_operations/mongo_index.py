from dotenv import load_dotenv
from pymongo import MongoClient,ASCENDING,DESCENDING
from pprint import pprint
from bson.objectid import ObjectId
from pymongo import ReturnDocument
from datetime import datetime
import os

load_dotenv()

MONGO_URI = str(os.getenv("MONGO_URI"))
client = MongoClient(MONGO_URI)

# CREATE AND READ
def connect(db_name):
    db = client[db_name]
 
    return db

# Single field index yaratma
def create_index():
    db = connect("sample_analytics")

    query = db.customers.create_index([("birthdate",ASCENDING)])

    return query


# Spesifik bir emaile göre arama yapamak istiyorsak
# email indexi yaratıp 
def create_email_index():
    db = connect("sample_analytics")
    query = db.customers.create_index([("email",ASCENDING)],unique = True)

    return query

print(create_email_index())

def get_indexes():
    db = connect("sample_analytics")
    query = db.customers.index_information()

    return query

# Multikey index
def create_multikey_index():
    db = connect("sample_analytics")
    query = db.customers.create_index([("accounts",ASCENDING)])

    return query


def compound_index():
    db = connect("sample_analytics")
    query = db.customers.find(
        filter = {"birthdate" : {"$gte" : datetime(1977,1,1)},"active" : True}
        ).sort([
            ("birthdate" , ASCENDING),
            ("name" , DESCENDING)
            ])

    return list(query)





    
    






