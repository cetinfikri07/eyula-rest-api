from datetime import datetime,date
from bson import json_util
import requests
import json
import os
from pprint import pprint

def default(self,obj):
    if isinstance(obj,(datetime,date)):
        return obj.isoformat()

    return json.JSONEncoder.default(self,obj)


with open("faker/employee_documents.json","r") as file:
    data = json.load(file)


url = "http://127.0.0.1:5555/api/v1/register-bulk"
headers = {"Content-Type": "application/json"}
response = requests.post(url,data = json.dumps(data,default=json_util.default),headers=headers)
pprint(response.json())

