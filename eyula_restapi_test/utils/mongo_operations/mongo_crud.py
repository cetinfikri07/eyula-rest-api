from dotenv import load_dotenv
from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId
from pymongo import ReturnDocument
from bson.objectid import ObjectId
from datetime import datetime
import os

load_dotenv()

MONGO_URI = str(os.getenv("MONGO_URI"))
client = MongoClient(MONGO_URI)

# CREATE AND READ
def connect(db_name):
    db = client[db_name]
 
    return db

def find_one():
    db = connect("sample_supplies")

    query = db.sales.find_one({
        "customer.email" : "cauho@witwuta.sv" 
        })
    pprint(query)


def elem_match():
    db = connect("sample_analytics")
    query = db.accounts.find({"products" : {"$elemMatch" : {"$eq" : "InvestmentStock"}}})

    pprint(list(query))


def multiple_elem_match():
    db = connect("sample_supplies")
    query = db.sales.find({
        "items" : {"$elemMatch" : {"name" : "laptop",
                                   "price" : {"$gt" : 800}, 
                                   "quantity" : {"$gte" : 1}}}
        })

    pprint(list(query))


def and_operator():
    db = connect("sample_airbnb")
    query = db.listingsAndReviews.find({
        "$and" : [{"room_type" : "Private room"},{"maximum_nights" : "360"}]
        })

    pprint(len(list(query)))


def or_operator():
    db = connect("sample_restaurants")
    query = db.restaurants.find({
        "$or" : [{"borough" : "Brooklyn"},{"cuisine" : "American"}]
        })

    pprint(list(query))

# UPDATE replace_one
def replace_one():
    db = connect("sample_mflix")
    query = db.comments.replace_one({
        "_id" : ObjectId("5a9427648b0beebeb69579e7"),
     },
        {
          "name": "Mercedes",
          "email": "mercedes_tyler@fakegmail.com",
          "movie_id": {
            "$oid": "573a1390f29313caabcd4323"
          },
          "text": "Eius veritatis vero facilis quaerat fuga temporibus. Praesentium expedita sequi repellat id. Corporis minima enim ex. Provident fugit nisi dignissimos nulla nam ipsum aliquam.",
          "date": {
            "$date": {
              "$numberLong": "1029646567000"
            }
          }
        }
    )

    result = {
        "matchedCount" : query.matched_count,
        "modifiedCount" : query.modified_count,
        "acknowledged" : query.acknowledged
        }

    print(result)
    
#update one 
def update_one():
    db = connect("sample_analytics")
    query = db.accounts.update_many(
            {"_id" : ObjectId("5ca4bbc7a2dd94ee5816238c")},
            {"$set" : {"limit" : 1500}}
        )

    result = {
        "matchedCount" : query.matched_count,
        "modifiedCount" : query.modified_count,
        "acknowledged" : query.acknowledged
        }

    print(result)

def upsert():
    db = connect("sample_mflix")
    query = db.users.update_one(
        {"name" : "Fikri Cetin"},
        {"$set" : {"password" : "1234"}},
        upsert = True
        )

    result = {
        "matchedCount" : query.matched_count,
        "modifiedCount" : query.modified_count,
        "acknowledged" : query.acknowledged
        }

    return result
     
def push():
    db = connect("sample_analytics")
    query = db.customers.update_one(
        {"_id" : ObjectId("5ca4bbcea2dd94ee58162a68")},
        {"$push" : {"accounts" : 542658}}
        )

    result = {
        "matchedCount" : query.matched_count,
        "modifiedCount" : query.modified_count,
        "acknowledged" : query.acknowledged
        }

    return result


def find_and_modify():
    db = connect("sample_analytics")
    query = db.transactions.find_one_and_update(
        filter = {"_id" : ObjectId("5ca4bbc1a2dd94ee58161cb1")},
        update = {"$inc" : {"transaction_count" : 1}},
        return_document = ReturnDocument.AFTER
        )

    return query

# UPDATE MANY
def update_many():
    db = connect("sample_analytics")
    query = db.customers.update_many(
        filter = {"birthdate" : {"$lt" : datetime(2000,1,1)}},
        update = {"$set" : {"address" : "0000 Bethany Glens Vasqueztown, CO 22939"}}
        )

    result = {
        "matchedCount" : query.matched_count,
        "modifiedCount" : query.modified_count,
        "acknowledged" : query.acknowledged
        }

    return result

# DELETE
# delete one 
def delete_one():
    db = connect("sample_analytics")
    query = db.customers.delete_one(
        filter = {"_id" : ObjectId("5ca4bbcea2dd94ee58162a68")}
        )

    result = {
        "acknowledged" : query.acknowledged,
        "deletedCount" : query.deleted_count
        }

    return result


#delete many
def delete_many():
    db = connect("sample_mflix")
    query = db.movies.delete_many(
        filter = {"title" : "The Great Train Robbery"}
        )

    result = {
        "acknowledged" : query.acknowledged,
        "deletedCount" : query.deleted_count
        }

    return result

def get_address_list():
    db = connect("eyula")
    result = db.companies.find_one(
        filter = {"companyName":"Google"},
        projection = {"addresses":True,"_id":0}
        )

    print(result.get("addresses"))

get_address_list() 































