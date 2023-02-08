from datetime import datetime,date
from bson import json_util
import requests
import json


def default(self,obj):
    if isinstance(obj,(datetime,date)):
        return obj.isoformat()

    return json.JSONEncoder.default(self,obj)

fikri = {
    "username":"cetin",
    "data" : {
        "country":"Turkey",
        "city":"Antalya",
        "district":"Konyaaltı Pınarbaşı",
        "street":"708 sk.",
        "buildingNumber":"5",
        "doorNumber":6,
        "coordinates":{
            "latitude":45.21,
            "longitude":33.25
            },
        "type":0,
        "status":True
        }
    }

jobs = {
    "username":"jobs",
    "data":{
        "country":"United State",
        "city":"California San Jose",
        "district":"San Pedro",
        "street":"745",
        "buildingNumber":"41",
        "doorNumber":8,
        "coordinates":{
            "latitude":45.21,
            "longitude":33.25
            },
        "type":1,
        "status":True
     }
    }


apple = {
    "company_name":"apple",
    "data":{
        "country":"United States",
        "city":"San Francisco",
        "district":"Sunny Vale",
        "street":"87",
        "buildingNumber":"12",
        "doorNumber":1,
        "coordinates":{
            "latitude":45.21,
            "longitude":33.25
            },
        "type":1,
        "status":True
     }
    }

url = "http://127.0.0.1:5555/api/v1/register-address"

headers = {"Content-Type": "application/json"}
response = requests.post(url,data = json.dumps(fikri, default=json_util.default),headers=headers)
print(response.json())

