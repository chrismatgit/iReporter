import unittest
# from api.routes import app
# from api.routes import app
# from flask import json
# from api.models import Incident
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from api.routes import app
from api.models import Incident

class TestIncident(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client()

    def test_add_incident(self):
        incident = {
                    "location": 121254154,
                    "createdBy": "1",
                    "incType": "red-flag",
                    "comment": "still under inverstigation",
                    "status": "under_investigation",
                    "video": "video.mp4",
                    "image": "image.jpg"
                    
                }
        response = self.tester.post(
            'api/v1/incident/', content_type ='application/json',
            data=json.dumps(incident)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn('incident created', reply['message'])
        self.assertEqual(response.status_code, 201)
    
    def test_incType_is_valid(self):
        incident = {
                    "location": 121254154,
                    "createdBy": "1",
                    "incType": "",
                    "comment": "still under inverstigation",
                    "status": "under_investigation",
                    "video": "video.mp4",
                    "image": "image.jpg"
                    
                }
        response = self.tester.post(
            'api/v1/incident/', content_type ='application/json',
            data=json.dumps(incident)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn('incType field can not be left empty or it should be eg: red-flag or intervention', reply['message'])
        self.assertEqual(response.status_code, 400)

    def test_image_is_valid(self):
        incident = {
                    "location": 121254154,
                    "createdBy": "1",
                    "incType": "red-flag",
                    "comment": "still under inverstigation",
                    "status": "under_investigation",
                    "video": "video.mp4",
                    "image": ""
                    
                }
        response = self.tester.post(
            'api/v1/incident/', content_type ='application/json',
            data=json.dumps(incident)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn('image field can not be left empty', reply['message'])
        self.assertEqual(response.status_code, 400)

    def test_video_is_valid(self):
        incident = {
                    "location": 121254154,
                    "createdBy": "1",
                    "incType": "red-flag",
                    "comment": "still under inverstigation",
                    "status": "under_investigation",
                    "video": "",
                    "image": "image.jpg"
                    
                }
        response = self.tester.post(
            'api/v1/incident/', content_type ='application/json',
            data=json.dumps(incident)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn('video field can not be left empty', reply['message'])
        self.assertEqual(response.status_code, 400)


    def test_comment_is_valid(self):
        incident = {
                    "location": 1212121,
                    "createdBy": "1",
                    "incType": "red-flag",
                    "comment": "",
                    "status": "under_investigation",
                    "video": "video.mp4",
                    "image": "image.jpg"
                    
                }
        response = self.tester.post(
            'api/v1/incident/', content_type ='application/json',
            data=json.dumps(incident)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn('comment field can not be left empty', reply['message'])
        self.assertEqual(response.status_code, 400)
    
    
    def test_status_is_valid(self):
        incident = {
                    "location": 1212121,
                    "createdBy": "1",
                    "incType": "red-flag",
                    "comment": "no comment",
                    "status": "",
                    "video": "video.mp4",
                    "image": "image.jpg"
                    
                }
        response = self.tester.post(
            'api/v1/incident/', content_type ='application/json',
            data=json.dumps(incident)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn('status field can not be left empty or it should be eg: draft, resolved, under_investigation or rejected', reply['message'])
        self.assertEqual(response.status_code, 400)
    
    def test_view_incidents(self):
        incident = {
                    "location": "12",
                    "createdBy": "1",
                    "incType": "red-flag",
                    "comment": "still under inverstigation",
                    "status": "under_investigation",
                    "video": "video.mp4",
                    "image": "image.jpg"
                    
                }
        response = self.tester.post(
            'api/v1/incident/', content_type ='application/json',
            data=json.dumps(incident)
        )
        reply = json.loads(response.data.decode())

        print(response.data)
        self.assertIn('incident created', reply['message'])
        self.assertEqual(response.status_code, 201)

        response = self.tester.get(
            'api/v1/incidents/', content_type = 'application/json'
        )
        reply = json.loads(response.data.decode())
        self.assertEqual(reply['Data'], get_inc)
        self.assertEqual(response.status_code, 200)
    
    