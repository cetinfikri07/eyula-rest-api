import json
from datetime import datetime
from faker import Faker
import os
from pprint import pprint
from bson import json_util
import requests

fake = Faker()

url = "http://127.0.0.1:5555/api/v1/register-bulk"
headers = {"Content-Type": "application/json"}

def default(self,obj):
    if isinstance(obj,(datetime,date)):
        return obj.isoformat()

    return json.JSONEncoder.default(self,obj)

def send_post(url,headers,data):
    response = requests.post(url,data = json.dumps(data,default=json_util.default),headers=headers)
    pprint(response.json())


def generate_customer(n_objects):
    data = []
    for i in range(n_objects):
        obj = {
            "customers" : {
                "firstName": fake.first_name(),
                "lastName": fake.last_name(),
                "username": fake.user_name(),
                "birthDate": str(fake.date_of_birth()),
                "gender": fake.random_int(min=0, max=1, step=1),
                "email": fake.email(),
                "profile": fake.image_url(),
                "phone": fake.phone_number(),
                "addresses": [],
                "bankAccounts": [],
                "ip": [fake.ipv4()],
                "status": fake.boolean(),
                "type": fake.random_int(min=0, max=1, step=1),
                "rDate": str(datetime.utcnow()),
                "uDate": str(datetime.utcnow()),
                "company": ["Google"]
            },

            "addresses": [
                {
                    "country": fake.country(),
                    "city": fake.city(),
                    "district": fake.state(),
                    "street": fake.building_number(),
                    "buildingNumber": fake.building_number(),
                    "doorNumber": fake.random_int(min=0, max=100, step=1),
                    "coordinates": {
                        "latitude": fake.pyfloat(left_digits=2, right_digits=2, min_value=-90, max_value=90),
                        "longitude": fake.pyfloat(left_digits=3, right_digits=2, min_value=-180, max_value=180)
                    },
                    "type": fake.random_int(min=0, max=1, step=1),
                    "status": True
                }
            ],

            "bank_accounts": [
                {
                    "bankName": fake.random_element(["Santander","Garanti BBVA","Ziraat Bankası","Bank of America"]),
                    "cardNumber": fake.credit_card_number(),
                    "cardExpire": fake.credit_card_expire(),
                    "cardType": fake.random_element(["Visa","MasterCard","American Express"]),
                    "currency": fake.random_element(["TRY","RUB","USD","EUR","GBP"]),
                    "type": fake.random_int(min=0, max=1, step=1),
                    "rDate": str(datetime.utcnow()),
                    "uDate": str(datetime.utcnow()),
                    "status": True
                }
            ]
            }

        data.append(obj)

    return data

def generate_company(n_objects):
    data = []
    for i in range(n_objects):
        obj = {
            "companies" : {
               "companyName": fake.random_element(["Microsoft","Apple","Amazon","Meta","Google"]),
                "employees": [],
                "taxNo": fake.msisdn(),
                "addresses": [],
                "email": fake.email(),
                "phone": fake.phone_number(),
                "status": True,
                "bankAccounts": [],
                "rDate": str(datetime.utcnow()),
                "uDate": str(datetime.utcnow())
            },

            "addresses": [
                {
                    "country": fake.country(),
                    "city": fake.city(),
                    "district": fake.state(),
                    "street": fake.building_number(),
                    "buildingNumber": fake.building_number(),
                    "doorNumber": fake.random_int(min=0, max=100, step=1),
                    "coordinates": {
                        "latitude": fake.pyfloat(left_digits=2, right_digits=2, min_value=-90, max_value=90),
                        "longitude": fake.pyfloat(left_digits=3, right_digits=2, min_value=-180, max_value=180)
                    },
                    "type": fake.random_int(min=0, max=1, step=1),
                    "status": True
                }
            ],

            "bank_accounts": [
                {
                    "bankName": fake.random_element(["Santander","Garanti BBVA","Ziraat Bankası","Bank of America"]),
                    "cardNumber": fake.credit_card_number(),
                    "cardExpire": fake.credit_card_expire(),
                    "cardType": fake.random_element(["Visa","MasterCard","American Express"]),
                    "currency": fake.random_element(["TRY","RUB","USD","EUR","GBP"]),
                    "type": fake.random_int(min=0, max=1, step=1),
                    "rDate": str(datetime.utcnow()),
                    "uDate": str(datetime.utcnow()),
                    "status": True
                }
            ]
            }
        
        data.append(obj)

    return data

def generate_employee(n_objects,locale):
    data = []
    for i in range(n_objects):
        fake.locale = locale
        obj = {
            "customers" : {
                "firstName": fake.first_name(),
                "lastName": fake.last_name(),
                "username": fake.user_name(),
                "birthDate": str(fake.date_of_birth()),
                "gender": fake.random_int(min=0, max=1, step=1),
                "email": fake.email(),
                "profile": fake.image_url(),
                "phone": fake.phone_number(),
                "addresses": [],
                "bankAccounts": [],
                "ip": [fake.ipv4()],
                "status": True,
                "type": fake.random_int(min=0, max=1, step=1),
                "rDate": str(datetime.utcnow()),
                "uDate": str(datetime.utcnow()),
                "company": ["Amazon EU"]
            }
        }

        data.append(obj)

    return data



bulk_customer = generate_customer(10)
bulk_company = generate_company(5)
bulk_employee = generate_employee(20,locale = "de_DE")


# save companies as json
with open("faker/employee_documents.json","w") as file:
    json.dump(bulk_employee,file,default = json_util.default)

