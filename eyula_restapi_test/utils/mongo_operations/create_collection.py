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

def create_customer_collection():
    db = connect("eyula")



