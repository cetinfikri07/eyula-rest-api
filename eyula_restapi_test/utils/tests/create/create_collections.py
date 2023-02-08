from datetime import datetime,date
from bson import json_util
import requests
import json

bulk_customer = [{
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
    "addresses":[{
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
        }],

    "bank_accounts":[{
            "bankName":"Santander",
            "cardNumber":"0000000000000000",
            "cardExpire":"04/27",
            "cardType":"Mastercad",
            "currency":"GBP",
            "type":0,
            "rDate":str(datetime.utcnow()),
            "uDate":str(datetime.utcnow()),
            "status":True
        }],
    }            
]

bulk_company = [{
    "companies":{
         "companyName":"Google",
         "employees":[],
         "taxNo":"0005",
         "addresses":[],
         "email":"info@google.com",
         "phone":"+905334529807",
         "status":True,
         "bankAccounts":[],
         "rDate":str(datetime.utcnow()),
         "uDate":str(datetime.utcnow())
        },
    "addresses":[{
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
        }],

    "bank_accounts":[{
            "bankName":"Santander",
            "cardNumber":"0000000000000000",
            "cardExpire":"04/27",
            "cardType":"Mastercad",
            "currency":"GBP",
            "type":0,
            "rDate":str(datetime.utcnow()),
            "uDate":str(datetime.utcnow()),
            "status":True
        }],
    }            
]



url = "http://127.0.0.1:5555/api/v1/register-bulk"
headers = {"Content-Type": "application/json"}
response = requests.post(url,data = json.dumps(bulk_company,default=json_util.default),headers=headers)
print(response.json())

