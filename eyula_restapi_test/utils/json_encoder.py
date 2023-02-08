import json
from bson.json_util import ObjectId
from datetime import datetime

class MyEncoder(json.JSONEncoder):
    def object_id(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(MyEncoder, self).default(obj) 
    def date(self,obj):
        if isinstance(obj,datetime):
            return obj.isoformat()

        return json.JSONEncoder.default(self,obj)


