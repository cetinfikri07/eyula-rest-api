from datetime import datetime,date
from bson import json_util
import requests
import json

fikri = {
    "username":"cetin.fikri",
    "address_id":"63e1f76b88f6db0ad94067eb"
    }

apple = {
    "company_name":"apple",
    "address_id":"63e1f79c4bd99b1f02111c5b"
    }


url = "http://127.0.0.1:5555/api/v1/remove-address"

headers = {"Content-Type": "application/json"}

response = requests.delete(url,data = json.dumps(apple),headers=headers)
print(response.json())


