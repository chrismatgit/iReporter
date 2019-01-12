import unittest
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from api import app
from api.Models.Users import User 
from base_test import BaseTest


class TestAuth(BaseTest):
    """Class tests registeration and login views"""

    def setUp(self):
        self.tester = app.test_client(self)
        self.accounts = User.accounts

    def test_successful_registration(self):
        """Test that a user can register successfully"""
        reply = self.login_user()
        token = reply['token']
        user = {
            "email": "kelly@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 2,
            "username": "kellym"
        }

        response = self.tester.post(
            '/api/v1/signup/',
            content_type='application/json',
            data=json.dumps(user),
            headers={'Authorization': f'Bearer {token}'}
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(reply['message'], 'mary has been created successfuly')
        self.assertEqual(response.status_code, 201)

    def test_user_can_login(self):
        # reply = self.login_user()
        # token = reply['token']
        user = {
            "email": "kelly1@example.com",
            "firstname": "mary",
            "isAdmin": False,
            "lastname": "grace",
            "othernames": "kelly",
            "password": "1212155454",
            "phone_number": "07512345678",
            "registered": "Wed, 12 Dec 2018 10:49:07 GMT",
            "user_id": 3,
            "username": "kellyma"
        }

        response = self.tester.post(
            '/api/v1/signup/',
            content_type='application/json',
            data=json.dumps(user),
            # headers={'Authorization': f'Bearer {token}'}
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(reply['message'], 'mary has been created successfuly')
        self.assertEqual(response.status_code, 201)

        user = {
            'username': 'kellyma',
            'password': '1212155454'
        }

        response = self.tester.post(
            '/api/v1/login/',
            content_type='application/json',
            data=json.dumps(user)
            # headers={'Authorization': f'Bearer {token}'}
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(reply['message'], 'kellyma successfuly login')
        self.assertEqual(response.status_code, 200)

    def test_welcome_message(self):
        reply = self.login_user()
        token = reply['token']
        response = self.tester.get(
            '/api/v1/welcome',
            content_type='application/json',
            headers={'Authorization': f'Bearer {token}'}
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(reply['message'], 'admin thanks for using iReporter Api')
        self.assertEqual(response.status_code, 200)



    def tearDown(self):
        User.accounts.clear()

