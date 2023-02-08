from flask import Blueprint,request,jsonify
from flask_restful import Resource
from bson import json_util
from pprint import pprint
import json

from eyula_restapi_test.shareddb import db
from eyula_restapi_test.companies import companies_service
from . import companies_bp

@companies_bp.route("/api/v1/register-companies",methods = ["POST"])
def register_companies():
    response = companies_service.register_companies(request)
    return response


@companies_bp.route("/api/v1/insert-employee",methods = ["POST"])
def insert_employees():
    response = companies_service.insert_employee(request)
    return response

@companies_bp.route("/api/v1/remove-company",methods = ["DELETE"])
def remove_company():
    response = companies_service.remove_company(request)
    return response





