from email_validator import validate_email,EmailNotValidError
import phonenumbers
from datetime import datetime
from pprint import pprint

class FieldValidators:
    def validate_objects(self,json_objects):
        valid_objects = []
        unvalid_objects = []
        error_messages = []
        for obj in json_objects:
            email = obj.get("email")
            phone = obj.get("phone")
            try:
                validate_mail = validate_email(email, check_deliverability=False)
                parsed_phone = phonenumbers.parse(phone,None)
                is_valid_phone = phonenumbers.is_valid_number(parsed_phone)

                if is_valid_phone is False:
                    raise Exception("Wrong phone number format")

                valid_objects.append(obj)
            except Exception as err:
                error_messages.append(err)
                unvalid_objects.append(obj)

        return error_messages,valid_objects,unvalid_objects

data = [
  {
    "companyName": "Facebook",
    "employees":[
        "63da21e4987ca6167b43888d",
        "63da23dc24d9847080b85e70"
        ],
    "taxNo":"0000",
    "addresses":["63da21e4987ca6167b43888c"],
    "email":"info@facebook.com",
    "phone":"+9005334529807",
    "rDate":datetime.utcnow(),
    "uDate":datetime.utcnow()
  },
  {
      "companyName" : "Twitter",
      "employees":[
          "63da23dc24d9847080b85e71",
          "63da23dc24d9847080b85e72"
          ],
      "taxNo":"0000",
      "addresses":["63da21e4987ca6167b43888p"],
      "email":"info@twitter.com",
      "phone":"+9005334529807",
      "rDate":datetime.utcnow(),
      "uDate":datetime.utcnow()
      }
]

validators = FieldValidators()
error_messages,valid_objects,unvalid_objects = validators.validate_objects(data)



























