from flask import Flask, jsonify, request
import datetime
import re



class Incident(object):
    
    incidents = [
            # {  
            #     "createdOn": "monday",
            #     "createdBy": 123,
            #     "incType": "red-flag",
            #     "location": "chris@gmail.com",
            #     "status": "draft",
            #     "image": "dechris",
            #     "video": "21/12/2018",
            #     "comment": "1212155454",
            #     "id": 1,
            #     "isadmin": False
            # }
        ]
   
    def __init__(self, createdOn, createdBy, incType, location, status, image, video,comment, id, isadmin):
        self.createdOn = createdOn
        self.createdBy = createdBy
        self.incType = incType
        self.location = location
        self.status = status
        self.image = image
        self.video = video
        self.comment = comment
        self.id = id
        self.isadmin = isadmin

    def validate_createdBy(self):
        if not self.createdBy or self.createdBy.isspace():
            return False
        else:
            return True

    def validate_incType(self):
        if not self.incType or self.incType.isspace() or not self.incType == "intervention" \
        and not self.incType == "red-flag":
            return False
        else:
            return True
    
    def validate_location(self):
        if not self.location or self.location.isspace() or not isinstance(int):
            return False
        else:
            return True

    def validate_status(self):
        if not self.status or self.status.isspace() or not self.status == "draft" \
        and not self.status == "under_investigation" and not self.status== "rejected" and not self.status=="resolved":
            return False
        else:
            return True

    def validate_image(self):
        if not self.image:
            return False
        else:
            return True

    def validate_video(self):
        if not self.video:
            return False
        else:
            return True
    
    def validate_comment(self):
        if not self.comment or self.comment.isspace():
            return False
        else:
            return True



class User(object):
    
    accounts = [
            {  
                "firstname": "christian",
                "lastname": "matab",
                "othername": "chris",
                "email": "chris@gmail.com",
                "phoneNumber": "0123456789",
                "username": "dechris",
                "registered": "21/12/2018",
                "password": "1212155454",
                "id": 1,
                "isadmin": False
            }
        ]
    def __init__(self, *args):
        self.firstname = args[0]
        self.lastname = args[1]
        self.othername = args[2]
        self.email = args[3]
        self.phoneNumber = args[4]
        self.username = args[5]
        self.registered = args[6]
        self.password = args[7]
        self.id = args[8]
        self.isadmin = args[9]


    def validate_firstname(self):
        if not self.firstname or self.firstname.isspace():
            return False  #'Firstname field can not be left empty'
        else:
            return True

    def validate_lastname(self):
        if not self.lastname or self.lastname.isspace():
            return False
        else:
            return True

    def validate_othername(self):
        if not self.othername or self.othername.isspace():
            return False
        else:
            return True
    
    def validate_email(self):
        if not self.email or self.email.isspace() or \
        not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", self.email):
            return False
        else:
            return True

    def validate_phoneNumber(self):
        if not self.phoneNumber or self.phoneNumber.isspace() or \
        len(self.phoneNumber)<9:
            return False
        else:
            return True

    def validate_username(self):
        if not self.username or self.username.isspace():
            return False
        else:
            return True

    def validate_registered(self):
        if not self.registered or self.registered.isspace():
            return False
        else:
            return True
    
    def validate_password(self):
        if not self.password or self.password.isspace() or \
        len(self.password) < 8:
            return False
        else:
            return True


