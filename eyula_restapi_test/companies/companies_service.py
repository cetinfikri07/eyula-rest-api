from flask import request,jsonify,Response,jsonify,make_response
from pymongo.errors import BulkWriteError
from bson import json_util
from pprint import pprint
import hashlib
import json

from eyula_restapi_test.shareddb import db
from eyula_restapi_test.utils.json_encoder import MyEncoder
from eyula_restapi_test.utils.validators import FieldValidators

def register_companies(request):
    validators = FieldValidators()

    try:
        new_companies = request.get_json()
        print(new_companies)

        if isinstance(new_companies,dict):
            new_companies = [new_companies]

        error_messages,valid_companies,unvalid_companies = validators.validate_objects(new_companies)
        print(error_messages)

        result = db.companies.insert_many(valid_companies)

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

def remove_company(request):
    try:
        data = request.get_json()
        company_name = data.get("company_name")
        # update status to true
        update_result = db.companies.update_one(
            filter = {"companyName": company_name},
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

def insert_employee(request):
    try:
        employee = request.get_json()
        username = employee.get("username")
        company = employee.get("company")

        #get customer_id
        customer_id = db.customers.find_one(
            filter = {"username":username},
            projection = {"_id" : True}
            )["_id"]

        customer_id = str(customer_id)

        #insert customer_id to companies.employees array
        update_result = db.companies.update_one(
            filter = {"companyName" : company},
            update = {"$push" : {"employees" : customer_id}}
            )

        result = {"acknowledged" : update_result.acknowledged,
                  "matchedCount" : update_result.matched_count,
                  "modifiedCount" : update_result.modified_count,
                  "status_code" : 200}

    except Exception as err:
        result = {
            "message" : f"Unexpected error: {err}",
            "status_code" : 500
            }

    response = Response(json.dumps(result,default=str),status=result["status_code"],mimetype="application/json")

    return response







