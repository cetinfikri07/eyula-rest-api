from datetime import datetime,date
from bson import json_util
import requests
import json


def default(self,obj):
    if isinstance(obj,(datetime,date)):
        return obj.isoformat()

    return json.JSONEncoder.default(self,obj)

fikri = {
    "firstName":"Fikri",
    "lastName":"Çetin",
    "username":"cetin",
    "birthDate": str(datetime(1998,4,21,0,0)),
    "gender":0,
    "email":"fikriceti@gmail.com",
    "profile":"fik.jpg",
    "phone":"+905334529317",
    "addresses":[],
    "bankAccounts":[],
    "ip":["122.52.65.125"],
    "status":True,
    "type":0,
    "rDate": str(datetime.utcnow()),
    "uDate": str(datetime.utcnow()),
    "deleted":False
    }

gates = {
    "firstName":"Bill",
    "lastName":"Gates",
    "username":"gates",
    "birthDate": str(datetime(1975,4,21,0,0)),
    "gender":1,
    "email":"bill@microsoft.com",
    "profile":"gates.jpg",
    "phone":"+905334529841",
    "addresses":[],
    "title":"CEO",
    "bankAccounts":[],
    "ip":["122.52.65.125"],
    "status":True,
    "type":1,
    "rDate": str(datetime.utcnow()),
    "uDate": str(datetime.utcnow()),
    "deleted":False
    }

all_collections = [{
    "customers":{
            "firstName":"James",
            "lastName":"Brown",
            "username":"jamesbrown",
            "birthDate": str(datetime(1977,4,21,0,0)),
            "gender":0,
            "email":"brownjames@gmail.com",
            "profile":"james.jpg",
            "phone":"+905334549831",
            "addresses":[],
            "bankAccounts":[],
            "ip":["122.52.65.125"],
            "status":True,
            "type":0,
            "rDate": str(datetime.utcnow()),
            "uDate": str(datetime.utcnow()),
            "company":["Microsoft"]
        },
    "address":{
            "country":"United States",
            "city":"New Jersey",
            "district":"Paterson",
            "street":"144",
            "buildingNumber":"12",
            "doorNumber":2,
            "coordinates":{
                "latitude":45.21,
                "longitude":33.25
                },
            "type":1,
            "status":True
        },

    "accounts":{
            "bankName":"Santander",
            "cardNumber":"0000000000000000",
            "cardExpire":"04/27",
            "cardType":"Mastercad",
            "currency":"GBP",
            "type":0,
            "rDate":str(datetime.utcnow()),
            "uDate":str(datetime.utcnow()),
            "status":True
        },
    }            
]



url = "http://127.0.0.1:5555/api/v1/register-customers"
headers = {"Content-Type": "application/json"}
response = requests.post(url,data = json.dumps(fikri, default=json_util.default),headers=headers)
print(response.json())
