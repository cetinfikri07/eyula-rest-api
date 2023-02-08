from datetime import datetime,date
from bson import json_util
import requests
import json

fikri = {
    "username":"cetin.fikri",
    "account_id":"63e1f898f887d9055f05955e"
    }

apple = {
    "company_name":"apple",
    "account_id":"63e1f8ba797f957a2a7e863a"
    }


url = "http://127.0.0.1:5555/api/v1/remove-account"

headers = {"Content-Type": "application/json"}

response = requests.delete(url,data = json.dumps(apple),headers=headers)
print(response.json())




