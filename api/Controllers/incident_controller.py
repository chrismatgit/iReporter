from flask import Flask, jsonify, request
from api.Models.Incidents import Incident
from api.Utilities.validations import Incident_validation
import datetime
from flask_jwt_extended import create_access_token

validator = Incident_validation()
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
        
        invalid_data = validator.add_incident_validation(createdBy, incType, location, status, image, video, comment)
        
        report = Incident(incident_id, createdOn, createdBy, incType, location, status, image, video, comment)
        if invalid_data:
            return jsonify(invalid_data), 400
        Incident.reports.append(report.__dict__)
        return jsonify({
            "status": 201,
            "data": report.__dict__,
            "message": f"{incType} has been created successfuly"
        }), 201
                                
        

    except Exception:
        return jsonify({
            'status': 400,
            'error': 'Something went wrong with your inputs'
        }), 400

def get_all_incidents():
    ''' Function enables the view of all the reports
    :returns:
    A list of all the incident created
    '''
    validator = Incident_validation.empty_incident(Incident.reports)
    if not validator:
        return jsonify({
            'status': 200,
            'data': [incident for incident in Incident.reports]
        }), 200
    else:
        return jsonify(validator), 400

def get_unique_red_flag(incident_id):
    ''' Function enables the view of a single red-flag record
    :param:
    incident_id - holds integer value of the id of the individual red-flag to be viewed
    :returns:
    Details of the red-flag whose id matches the one entered.
    '''
    try:
        validator = Incident_validation.empty_incident(Incident.reports)
        if not validator:
            return jsonify({
                'status': 200,
                'data': next(incident for incident in Incident.reports if incident['incident_id'] == incident_id),
                'message': 'incidents fetched'
            }), 200
        else:
            return jsonify(validator), 400
    except IndexError:
        return jsonify({
            'message': 'incident does not exit or check your id',
            'status': 404
        }), 404

def update_red_flag_loc(incident_id):
    ''' Function enables the user to update a single red-flag record location
    :param:
    incident_id - holds integer value of the id of the individual red-flag to be updated
    :returns:
    A success message and the Details of the red-flag whose id matches the one entered and update the location if the incType equal red-flag.
    '''
    try:
        validator = Incident_validation.empty_incident(Incident.reports)
        if not validator:
            data = request.get_json()
            location = data.get("location")
            val = Incident_validation.validate_red_flag_location(location)
            if not val:
                red_flag = next(incident for incident in Incident.reports if incident['incident_id'] == incident_id)
                if red_flag['incType'] == 'red-flag':
                    red_flag['location'] = location
                    return jsonify({
                        'status': 200,
                        'message': 'location updated successfully'
                    }), 200
            else:
                return jsonify(val), 400
            
        else:
            return jsonify(validator), 400
    except Exception:
        return jsonify({
            'status': 400,
            'error': 'Something went wrong with your inputs or check your id in the URL'
        }), 400

def update_red_flag_com(incident_id):
    ''' Function enables the user to update a single red-flag record comment
    :param:
    incident_id - holds integer value of the id of the individual red-flag to be updated
    :returns:
    A success message and the Details of the red-flag whose id matches the one entered and update the comment if the incType equal red-flag.
    '''
    try:
        validator = Incident_validation.empty_incident(Incident.reports)
        if not validator:
            data = request.get_json()
            comment = data.get("comment")
            val = Incident_validation.validate_red_flag_comment(comment)
            if not val:
                red_flag = next(incident for incident in Incident.reports if incident['incident_id'] == incident_id)
                if red_flag['incType'] == 'red-flag':
                    red_flag['comment'] = comment
                    return jsonify({
                        'status': 200,
                        'message': 'comment updated successfully'
                    })
            else:
                return jsonify(val), 400
        else:
            return jsonify(validator), 400
    except Exception:
        return jsonify({
            'status': 400,
            'error': 'Something went wrong with your inputs or check your id in the URL'
        }), 400

def delete_red_flag(incident_id):
    ''' Function enables a user to delete a single incident record
    :param:
    incident_id - holds integer value of the id of the individual incident to be deleted
    :returns:
    the success message and the Details of the incident whose id matches the one entered to be deleted.
    '''
    try:
        validator = Incident_validation.empty_incident(Incident.reports)
        if not validator:
            incident = next(incident for incident in Incident.reports if incident['incident_id'] == incident_id)
            if incident:
                Incident.reports.remove(incident)
                return jsonify({
                    'status': 200,
                    'data': incident,
                    'message': 'incident deleted'
                }), 200
            else:
                return jsonify({
                'status': 400,
                'error': 'invalid incident'
            }), 400
        else:
            return jsonify(validator), 400
    except Exception:
        return jsonify({
            'message': 'incident does not exit or check your id',
            'status': 404
        }), 404