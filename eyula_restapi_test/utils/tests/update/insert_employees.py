from datetime import datetime,date
from bson import json_util
import requests
import json

def default(self,obj):
    if isinstance(obj,(datetime,date)):
        return obj.isoformat()

    return json.JSONEncoder.default(self,obj)

gates = {
    "username":"gates",
    "company":"Microsoft"
    }



url = "http://127.0.0.1:5555/api/v1/insert-employee"
headers = {"Content-Type": "application/json"}
response = requests.post(url,data = json.dumps(gates, default=json_util.default),headers=headers)
print(response.json())

