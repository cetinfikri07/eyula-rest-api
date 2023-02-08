from datetime import datetime,date
from bson import json_util
import requests
import json


def default(self,obj):
    if isinstance(obj,(datetime,date)):
        return obj.isoformat()

    return json.JSONEncoder.default(self,obj)

microsoft = {
     "companyName":"Microsoft",
     "employees":[],
     "taxNo":"0004",
     "addresses":[],
     "email":"info@microsoft.com",
     "phone":"+905334529803",
     "status":True,
     "bankAccounts":[],
     "rDate":str(datetime.utcnow()),
     "uDate":str(datetime.utcnow())
    }


url = "http://127.0.0.1:5555/api/v1/register-companies"

headers = {"Content-Type": "application/json"}
response = requests.post(url,data = json.dumps(microsoft, default=json_util.default),headers=headers)
print(response.json())


