from datetime import datetime,date
from bson import json_util
import requests
import json

jobs = {
    "username":"jobs",
    }

url = "http://127.0.0.1:5555/api/v1/remove-customer"

headers = {"Content-Type": "application/json"}

response = requests.delete(url,data = json.dumps(jobs),headers=headers)
print(response.json())

