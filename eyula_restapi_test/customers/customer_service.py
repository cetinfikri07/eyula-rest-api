from flask import request,jsonify,Response,jsonify,make_response
from email_validator import validate_email,EmailNotValidError
from pymongo.errors import BulkWriteError
from bson.objectid import ObjectId
from bson import json_util
from pprint import pprint
import hashlib
import json
import sys
import os

from eyula_restapi_test.shareddb import db
from eyula_restapi_test.utils.json_encoder import MyEncoder
from eyula_restapi_test.utils.validators import FieldValidators

def register_customers(request):
    validators = FieldValidators()
   
    try:
        new_customers = request.get_json()

        if isinstance(new_customers,dict):
            new_customers = [new_customers]

        #validate email and phone
        error_messages,valid_customers,unvalid_customers = validators.validate_objects(new_customers)

        result = db.customers.insert_many(valid_customers)

        result = {
            "acknowledged" : result.acknowledged,
            "insertedIds" : result.inserted_ids,
            "status_code" : 200,
            "messages" : error_messages
            }

    except BulkWriteError as err:
        err = err.details["writeErrors"][0]
        result = {
               "message" : f"Bulk write error: {err}",
               "status_code" : 500
                  }       
    except Exception as err:
        result = {
            "message" : f"Unexpected error: {err}",
            "status_code" : 500
            }

    response = Response(json.dumps(result,default=str),status=result["status_code"],mimetype="application/json")


    return response

def register_address(request):

    try:
        address = request.get_json()
        username = address.get("username")
        company_name = address.get("company_name")

        #insert address collection
        insert_result = db.addresses.insert_one(address["data"])
        address_id = str(insert_result.inserted_id)

        #decide customer or company 
        if username:
            #update customer collection
            update_result = db.customers.update_one(
                filter = {"username" : username},
                update = {"$push" : {"addresses" : address_id}}
                )
        else:
            # update company collection
            update_result = db.companies.update_one(
                    filter = {"companyName":company_name},
                    update = {"$push" : {"addresses" : address_id}}
                    )


        result = {"acknowledgedAddress" : insert_result.acknowledged,
                  "acknowledgedObject" : update_result.acknowledged,
                  "insertedAddressId": insert_result.inserted_id,
                  "matchedObject" : update_result.matched_count,
                  "modifiedObject" : update_result.modified_count,
                  "status_code" : 200}

    except Exception as err:
        result = {
            "message" : f"Unexpected error:{err}",
            "status_code":500
            }

    response = Response(json.dumps(result,default=str),status=result["status_code"],mimetype="application/json")

    return response
    
def register_accounts(request):
    try:
        account = request.get_json()
        username = account.get("username")
        company_name = account.get("company_name")

        #insert account
        insert_result = db.bank_accounts.insert_one(account["data"])
        account_id = str(insert_result.inserted_id)

        if username:
            #update customer collection
            update_result = db.customers.update_one(
                filter = {"username" : username},
                update = {"$push" : {"bankAccounts" : account_id}}
                )
        else:
            #update companies collection
            update_result = db.companies.update_one(
                filter = {"username" : username},
                update = {"$push" : {"bankAccounts" : account_id}}
                )


        result = {"acknowledgedAccount" : insert_result.acknowledged,
                  "acknowledgedObject" : update_result.acknowledged,
                  "insertedAccountId": insert_result.inserted_id,
                  "matchedObject" : update_result.matched_count,
                  "modifiedObject" : update_result.modified_count,
                  "status_code" : 200}

    except Exception as err:
            result = {
                "message" : f"Unexpected error:{err}",
                "status_code" : 500
                }

    response = Response(json.dumps(result,default=str),status=result["status_code"],mimetype="application/json")

    return response

def register_bulk(request):
    try:
        data = request.get_json()
        for obj in data:
            key = "customers" if "customers" in obj else "companies"
            user = obj[key]
            addresses = obj["addresses"]
            accounts = obj["bank_accounts"]

            #insert customer
            user.pop("company",None)
            user_result = db[key].insert_one(user)
            user_id = user_result.inserted_id

            #insert address
            address_insert_result = db.addresses.insert_many(addresses)
            address_ids = [str(_id) for _id in address_insert_result.inserted_ids]

            #push address id to user
            address_update_result = db[key].update_one(
                filter = {"_id" : user_id},
                update = {"$push" : {"addresses" : {"$each" : address_ids}}}
                )

            #insert accounts 
            account_insert_result = db.bank_accounts.insert_many(accounts)
            account_ids = [str(_id) for _id in account_insert_result.inserted_ids]

            #push account_ids to user
            account_update_result = db[key].update_one(
                filter = {"_id" : user_id},
                update = {"$push" : {"bankAccounts" : {"$each" : account_ids}}}
                )

            #insert account 

        result = {
            "status_code":200,
            "insertedUserId":user_id,
            "insertedAddressIds":address_ids,
            "insertedAccountIds":account_ids,
            "macthedAddressCount":address_update_result.matched_count,
            "modifiedAddressCount":address_update_result.modified_count,
            "matchedAccountCount":account_update_result.matched_count,
            "modifiedAccountCount":account_update_result.modified_count
            }

    except Exception as err:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            result = {
                "message" : f"Unexpected error:{err}",
                "status_code" : 500
                }

    response = Response(json.dumps(result,default=str),status=result["status_code"],mimetype="application/json")

    return response


def remove_customer(request):
    try:
        data = request.get_json()
        username = data.get("username")
        print(username)

        # update status to true
        update_result = db.customers.update_one(
            filter = {"username": username},
            update = {"$set": {"status" : False}}
            )

        result = {"acknowledged_update" : update_result.acknowledged,
                  "matched_count" : update_result.matched_count,
                  "modified_count" : update_result.modified_count,
                  "status_code" : 200}

    except Exception as err:
        result = {
            "message":f"Unexpected error:{err}",
            "status_code":500
            }

    response = Response(json.dumps(result,default=str),status=result["status_code"],mimetype="application/json")

    return response


def remove_address(request):
    try:
        data = request.get_json()
        address_id = data.get("address_id")
        username = data.get("username")
        company_name = data.get("company_name")

        # update deleted to true
        update_result = db.addresses.update_one(
            filter = {"_id": ObjectId(address_id)},
            update = {"$set": {"status" : False}}
            )

        """ 
        if username:
            #pull address_id from customer collection
            update_result = db.customers.update_one(
                filter = {"username" : username},
                update = {"$pull" : {"addresses" : address_id}}
                )
        else:
            #pull address_id from companies collection
            update_result = db.companies.update_one(
                filter = {"companyName" : company_name},
                update = {"$pull" : {"addresses" : address_id}}
                ) 
        """


        result = {"acknowledged_update" : update_result.acknowledged,
                  "matched_count" : update_result.matched_count,
                  "modified_count" : update_result.modified_count,
                  "status_code" : 200}

    except Exception as err:
        result = {
            "message":f"Unexpected error:{err}",
            "status_code":500
            }

    response = Response(json.dumps(result,default=str),status=result["status_code"],mimetype="application/json")

    return response

def remove_accounts(request):
    try:
        data = request.get_json()
        account_id = data.get("account_id")
        username = data.get("username")
        company_name = data.get("company_name")

        #delete from accounts collection
        update_result = db.bank_accounts.update_one(
            filter = {"_id": ObjectId(account_id)},
            update = {"$set": {"status" : False}}
            )
        """ 
        if username:
            #pull address_id from customer collection
            update_result = db.customers.update_one(
                filter = {"username" : username},
                update = {"$pull" : {"bankAccounts" : account_id}}
                )
        else:
            update_result = db.companies.update_one(
                filter = {"companyName" : company_name},
                update = {"$pull" : {"bankAccounts" : account_id}}
                )
        """

        result = {"acknowledged_update" : update_result.acknowledged,
                  "matched_count" : update_result.matched_count,
                  "modified_count" : update_result.modified_count,
                  "status_code" : 200}

    except Exception as err:
        result = {
            "message":f"Unexpected error:{err}",
            "status_code":500
            }

    response = Response(json.dumps(result,default=str),status=result["status_code"],mimetype="application/json")

    return response

def activate_collections(request):
    try:
        data = request.get_json()
        collection = data.get("collection_name")
        string_ids = data.get("_id")
        print(collection)

        #converst list of string ids to object_ids
        object_ids = [ObjectId(id) for id in string_ids]

        # set status to true
        set_status = {"$set": {"status" : True}} 

        update_result = db[collection].update_many(
            filter = {"_id": {"$in" : object_ids}},
            update = set_status
            )

        result = {"acknowledged_update" : update_result.acknowledged,
                  "matched_count" : update_result.matched_count,
                  "modified_count" : update_result.modified_count,
                  "status_code" : 200}

    except Exception as err:
        result = {
            "message":f"Unexpected error:{err}",
            "status_code":500
            }

    response = Response(json.dumps(result,default=str),status=result["status_code"],mimetype="application/json")

    return response


    





        












      



