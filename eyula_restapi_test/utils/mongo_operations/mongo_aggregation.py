from dotenv import load_dotenv
from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId
from pymongo import ReturnDocument
from datetime import datetime
from bson import SON
import os

load_dotenv()

MONGO_URI = str(os.getenv("MONGO_URI"))
client = MongoClient(MONGO_URI)

def connect(db_name):
    db = client[db_name]
 
    return db

def match():
    db = connect("sample_training")
    
    query = db.zips.aggregate(
        pipeline = [
            {"$match" : {"state" : "CA"}}, # match stage
            {"$group" : {                  # group stage
                    "_id" : "$city",
                    "totalZips" : {"$count" : {}}
                }},
            {"$sort" : SON([("totalZips",-1)])},
            {"$limit" : 5}
            ]
        )

    return query

def projection():
    db = connect("sample_training")

    query = db.zips.aggregate(
        pipeline = [
            {"$project" : 
                {"state" : True, "zip" : True, "population" : "$pop","_id" : False}
             }
            ]
        )

    return list(query)

def set():
    """
    Adds or modifies fields in the pipeline
    """
    # multiply population growth and population
    db = connect("sample_training")
    query = db.zips.aggregate(
        pipeline = [
            {"$set" : {"pop_2022" : {"$round" : {"$multiply" : [1.0031,"$pop"]}}}},
            {"$limit" : 5}
            ]
        )

    return list(query)

def out():
    """
    Writes the documents that are returned by an aggregation pipeline into a collection
    Must be the last stage
    Creates a new collection if it does not already exist
    If collection exits, $out replaces the existing collection with new data
    """
    db = connect("sample_training")
    query = db.zips.aggregate(
        pipeline = [
                {"$group" : {"_id" : "$state","total_pop" : {"$sum" : "$pop"}}},
                {"$match" : {"total_pop" : {"$lt" : 1000000}}},
                {"$out" : "small_states"}
            ]
        )

    return list(query)

pprint(out())


    


    

