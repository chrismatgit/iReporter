import json
import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from api import app
from api.Models import Users


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)

    def login_user(self):
        """Base method for logging in a user"""

        user = {
            "email": "admin@example.com",
            "firstname": "admin",
            "isAdmin": False,
            "lastname": "admin",
            "othernames": "admin",
            "password": "admin123",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 1,
            "username": "admin"
        }
        response = self.tester.post(
            '/api/v1/signup/',
            content_type='application/json',
            data=json.dumps(user)
        )

        user = dict(
            username='admin',
            password='admin123'
        )

        response = self.tester.post(
            '/api/v1/login/',
            content_type='application/json',
            data=json.dumps(user)
        )

        reply = json.loads(response.data.decode())

        return reply
