import unittest
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from api.routes import app
from api.models import User

class TestIncident(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client()

    def test_add_account(self):
        account = {
            "email": "example@gmail.com",
            "firstname": "christian",
            "lastname": "matab",
            "othername": "chris",
            "password": "1212155454",
            "phoneNumber": "0123456789",
            "registered": "21/12/2018",
            "username": "dechris"
            
            }
        response = self.tester.post(
            '/api/v1/signUp/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn('account created', reply['message'])
        self.assertEqual(response.status_code, 201)

    def test_email_is_valid(self):
        account = {
            "email": "examplegmail.com",
            "firstname": "christian",
            "lastname": "matab",
            "othername": "chris",
            "password": "1212155454",
            "phoneNumber": "0123456789",
            "registered": "21/12/2018",
            "username": "dechris"
            
            }
        response = self.tester.post(
            '/api/v1/signUp/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn('Email field can not be left empty or is invalid(eg: example@example.com)', reply['message'])
        self.assertEqual(response.status_code, 400)

    def test_firstname_is_valid(self):
        account = {
            "email": "example@gmail.com",
            "firstname": "",
            "lastname": "matab",
            "othername": "chris",
            "password": "1212155454",
            "phoneNumber": "0123456789",
            "registered": "21/12/2018",
            "username": "dechris"
            
            }
        response = self.tester.post(
            '/api/v1/signUp/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn('Firstname field can not be left empty', reply['message'])
        self.assertEqual(response.status_code, 400)



    def test_lastname_is_valid(self):
        account = {
            "email": "example@gmail.com",
            "firstname": "christian",
            "lastname": "",
            "othername": "chris",
            "password": "1212155454",
            "phoneNumber": "0123456789",
            "registered": "21/12/2018",
            "username": "dechris"
            
            }
        response = self.tester.post(
            '/api/v1/signUp/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn('Lastname field can not be left empty', reply['message'])
        self.assertEqual(response.status_code, 400)



    def test_othername_is_valid(self):
        account = {
            "email": "examplegmail.com",
            "firstname": "christian",
            "lastname": "matab",
            "othername": "",
            "password": "1212155454",
            "phoneNumber": "+25623456789",
            "registered": "21/12/2018",
            "username": "dechris"
            
            }
        response = self.tester.post(
            '/api/v1/signUp/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn('othername field can not be left empty', reply['message'])
        self.assertEqual(response.status_code, 400)


    def test_password_is_valid(self):
        account = {
            "email": "example@gmail.com",
            "firstname": "christian",
            "lastname": "matab",
            "othername": "chris",
            "password": "",
            "phoneNumber": "+25623456789",
            "registered": "21/12/2018",
            "username": "dechris"
            
            }
        response = self.tester.post(
            '/api/v1/signUp/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn('Password field can not be left empty or is less than 8', reply['message'])
        self.assertEqual(response.status_code, 400)


    def test_phoneNumber_is_valid(self):
        account = {
            "email": "example@gmail.com",
            "firstname": "christian",
            "lastname": "matab",
            "othername": "chris",
            "password": "12345624",
            "phoneNumber": "",
            "registered": "21/12/2018",
            "username": "dechris"
            
            }
        response = self.tester.post(
            '/api/v1/signUp/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn('phoneNumber field can not be left empty and should be more than 9', reply['message'])
        self.assertEqual(response.status_code, 400)


    def test_username_is_valid(self):
        account = {
            "email": "example@gmail.com",
            "firstname": "christian",
            "lastname": "matab",
            "othername": "chris",
            "password": "12345624",
            "phoneNumber": "+2656565987",
            "registered": "21/12/2018",
            "username": ""
            
            }
        response = self.tester.post(
            '/api/v1/signUp/', content_type ='application/json',
            data=json.dumps(account)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn('Username field can not be left empty', reply['message'])
        self.assertEqual(response.status_code, 400)