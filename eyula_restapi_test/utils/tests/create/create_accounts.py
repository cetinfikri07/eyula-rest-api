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
    "data":{
        "bankName":"Ziraat Bankası",
        "cardNumber":"0000000000000000",
        "cardExpire":"05/27",
        "cardType":"Mastercad",
        "currency":"GBP",
        "type":0,
        "rDate":str(datetime.utcnow()),
        "uDate":str(datetime.utcnow()),
        "status":True
        }
    }

jobs = {
    "username":"jobs",
    "data":{
            "bankName":"Bank of America",
            "cardNumber":"0000000000000000",
            "cardExpire":"08/26",
            "cardType":"Visa",
            "currency":"USD",
            "type":1,
            "rDate":str(datetime.utcnow()),
            "uDate":str(datetime.utcnow()),
            "status":True
        }
    }

apple = {
    "company_name":"apple",
    "data":{
        "bankName":"Sandanter",
        "cardNumber":"0000000000000000",
        "cardExpire":"08/25",
        "cardType":"MasterCard",
        "currency":"USD",
        "type":1,
        "rDate":str(datetime.utcnow()),
        "uDate":str(datetime.utcnow()),
        "status":True
        }
    }


url = "http://127.0.0.1:5555/api/v1/register-accounts"
headers = {"Content-Type": "application/json"}
response = requests.post(url,data = json.dumps(fikri, default=json_util.default),headers=headers)
print(response.json())
