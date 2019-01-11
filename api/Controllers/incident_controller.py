from flask import Flask, jsonify, request
from api.Models.Incidents import Incident
from api.Utilities.validations import Incident_validation
import datetime
from flask_jwt_extended import create_access_token

def create_incident():
    '''Function creates a new incident to the reports list
    :returns:
    a success message and the incident.
    '''
    try:
        data = request.get_json()
        incident_id = len(Incident.reports)+1
        createdOn = datetime.datetime.now()
        createdBy = data.get("createdBy")
        incType = data.get("incType")
        location = data.get("location")
        status = data.get("status")
        image = data.get("image")
        video = data.get("video")
        comment = data.get("comment")

        # validation
        validator = Incident_validation(createdBy, incType, location, status, image, video, comment)
        invalid_createdBy = validator.validate_createdBy()
        invalid_incType = validator.validate_incType()
        invalid_location = validator.validate_location()
        invalid_status = validator.validate_status()
        invalid_image = validator.validate_image()
        invalid_video = validator.validate_video()
        invalid_comment = validator.validate_comment()
        
        report = Incident(incident_id, createdOn, createdBy, incType, location, status, image, video, comment)

        if not invalid_createdBy:
            if not invalid_incType:
                if not invalid_location:
                    if not invalid_status:
                        if not invalid_image:
                            if not invalid_video:
                                if not invalid_comment:

                                        Incident.reports.append(report.__dict__)
                                        return jsonify({
                                            "status": 201,
                                            "data": report.__dict__,
                                            "message": f"{incType} has been created successfuly"
                                        }), 201
                                return jsonify(invalid_comment), 400
                            return jsonify(invalid_video), 400
                        return jsonify(invalid_image), 400
                    return jsonify(invalid_status), 400
                return jsonify(invalid_location), 400
            return jsonify(invalid_incType), 400
        return jsonify(invalid_createdBy), 400

    except Exception:
        return jsonify({
            'status': 400,
            'error': 'Something went wrong with your inputs'
        }), 400

