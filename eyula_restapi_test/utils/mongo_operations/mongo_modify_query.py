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

# SORTING AND LIMITING

def connect(db_name):
    db = client[db_name]
    return db

def sort_and_limit():
    db = connect("sample_training")
    query = db.companies.find(
        filter = {"category_code" : "music"}
        ).sort(
            "name",ASCENDING
            ).limit(10)

    return query


def sort_project():
    db = connect("sample_training")
    query = db.companies.find(
        filter = {"category_code" : "music"},
        projection = {"name" : True, "number_of_employees": True}
        ).sort(
            "number_of_employees",DESCENDING
            ).limit(3)

    return query


def projection():
    db = connect("sample_training")
    query = db.inspections.find(
        filter = {"sector" : "Restaurant - 818"},
        projection = {"business_name" : True,"result" : True,"_id" : False}
        ).limit(5)

    return list(query)


def include():
    db = connect("sample_training")
    query = db.inspections.find(
        filter = {"result" : {"$in" : ["Pass","Warning"]}},
        projection = {"_id" : False,"address.zip" : False, "certificate_number" : False}
        ).limit(5)

    return list(query)

def count_documents():
    db = connect("sample_training")
    query = db.trips.count_documents(
        filter = {
            "tripduration" : {"$gt" : 120},
            "usertype" : "Subscriber"
            }
        )
       
    return query


print(count_documents())


