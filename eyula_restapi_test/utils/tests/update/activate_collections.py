from datetime import datetime,date
from bson import json_util
import requests
import json


def activate_customers(url,data,headers):
    response = requests.post(url,data = json.dumps(data),headers=headers)
    print(response.json())

data = {
    "collection_name" : "addresses",
     "_id" : ["63e1f76b88f6db0ad94067eb","63e1f79c4bd99b1f02111c5b"]
    }
 
url = "http://127.0.0.1:5555/api/v1/activate"
headers = {"Content-Type": "application/json"}

activate_customers(url,data,headers)

