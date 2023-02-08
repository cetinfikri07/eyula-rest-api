from datetime import datetime,date
from bson import json_util
import requests
import json

company = {
    "company_name":"Microsoft",
    }


url = "http://127.0.0.1:5555/api/v1/remove-company"

headers = {"Content-Type": "application/json"}

response = requests.delete(url,data = json.dumps(company),headers=headers)
print(response.json())



