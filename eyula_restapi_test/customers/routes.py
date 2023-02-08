from flask import Blueprint,request,jsonify
from flask_restful import Resource
from bson import json_util
from pprint import pprint
import json

from eyula_restapi_test.shareddb import db
from eyula_restapi_test.customers import customer_service
from . import customers_api
from . import customers_bp


# CREATE 
@customers_bp.route("/api/v1/register-customers",methods = ["POST"])
def register_customers():
    response = customer_service.register_customers(request)
    return response

@customers_bp.route("/api/v1/register-address",methods=["POST"])
def register_address():
    response = customer_service.register_address(request)
    return response


@customers_bp.route("/api/v1/register-accounts",methods = ["POST"])
def register_accounts():
    response = customer_service.register_accounts(request)
    return response

@customers_bp.route("/api/v1/register-bulk",methods = ["POST"])
def register_bulk():
    response = customer_service.register_bulk(request)
    return response


# DELETE
@customers_bp.route("/api/v1/remove-customer",methods=["DELETE"])
def remove_customer():
    response = customer_service.remove_customer(request)
    return response

@customers_bp.route("/api/v1/remove-address",methods=["DELETE"])
def remove_address():
    response = customer_service.remove_address(request)
    return response

@customers_bp.route("/api/v1/remove-account",methods=["DELETE"])
def remove_accounts():
    response = customer_service.remove_accounts(request)
    return response

@customers_bp.route("/api/v1/activate",methods=["POST"])
def activate_collections():
    response = customer_service.activate_collections(request)
    return response



# READ
@customers_bp.route("/api/v1/customer/<int:customer_id>",methods = ["GET","POST"])
def fetch_customer(customer_id):
    customer = db.customers.find_one({"id" : customer_id})
    return jsonify(customer)

# UPDATE
@customers_bp.route("/api/v1/customer/<int:customer_id>",methods = ["POST"])
def update_customer(customer_id):
    customer = db.customers.find_one({"id" : customer_id})
  


# LOGIN
@customers_bp.route("/api/v1/login",methods=["POST"])
def login():
    response = customer_service.login(request)
    return jsonify(response)

    

















