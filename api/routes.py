from flask import Flask, jsonify, request
import datetime
from api.models import Incident, User
# from api.validations import Users_validation
# from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity

app = Flask(__name__)

@app.route('/')
def welcome():
    return "welcome"

@app.route('/api/v1/incident/', methods=['POST'])
def add_Incident():

    try: 
        data = request.get_json()
        createdBy = data.get('createdBy')
        incType = data.get('incType')
        location = data.get('location')
        status = data.get('status')
        image = data.get('image')
        video = data.get('video')
        comment = data.get('comment')
        id = len(Incident.incidents)+1
        isadmin = False
        createdOn = datetime.datetime.now()

        incident = Incident(createdOn, createdBy, incType, location,\
         status, image, video, comment, id, isadmin)

        
        if incident.validate_createdBy() is False:
            return jsonify({
                'message': 'createdBy field can not be left empty'
            }), 400
        if incident.validate_incType() is False:
            return jsonify({
                'message': 'incType field can not be left empty or it should be eg: red-flag or intervention'
            }), 400
        if incident.validate_location is False:
            return jsonify({
                'message': 'location field can not be left empty'
            }), 400
        if incident.validate_status() is False:
                return jsonify({
                'message':'status field can not be left empty or it should be eg: draft, resolved, under_investigation or rejected'
            }), 400
        if incident.validate_image() is False:
                return jsonify({
                'message': 'image field can not be left empty'
            }), 400
        if incident.validate_video() is False:
            return jsonify({
                'message': 'video field can not be left empty'
            }), 400
        if incident.validate_comment() is False:
            return jsonify({
                'message': 'comment field can not be left empty'
            }), 400
        
        Incident.incidents.append(incident.__dict__)
        return jsonify({
            'status': 201,
            'Data': incident.__dict__,
            'message': 'incident created'
            }), 201
    except Exception:
        return jsonify({'message': 'Something went wrong with your inputs'}), 400


@app.route('/api/v1/incidents/', methods=['GET'])
def get_incidents():
    if len(Incident.incidents) == 0:
        return jsonify({
            'message': 'There are no user yet!'
        }), 400

    return jsonify({
        'status': 200,
        'Data': [incident for incident in Incident.incidents]
    }), 200

@app.route('/api/v1/incident/<int:id>', methods=['GET'])
def get_single_incicent(id):
    try:
        if len(Incident.incidents) == 0:
            return jsonify({
                'message': 'There are no incident yet!',
                'status': 404
            }), 404
        incident = Incident.incidents[id-1]
        return jsonify({
            'Incident': incident,
            'message': 'incident fetched'
        })
    except IndexError:
        return jsonify({
            'message': 'incident does not exit or check your id',
            'status': 404
        }), 404

@app.route('/api/v1/edit_location/<int:id>', methods=['PATCH'])
def update_incicent_location(id):
    try:
  
        data = request.get_json()
        location = data.get('location')
        
        if len(Incident.incidents) == 0:
            return jsonify({
                'message': 'There are no incident yet!',
                'status': 404
            }), 404
        incident = Incident.incidents[id-1]
        for incident in Incident.incidents:
            if incident["id"] == id:
                incident['location'] = location

        return jsonify({
                'status': 200,
                'data': incident,
                'message': 'incident location updated'
            }), 200
    except IndexError:
        return jsonify({
            'message': 'incident does not exit or check your id',
            'status': 404
        }), 404



@app.route('/api/v1/edit_comment/<int:id>', methods=['PATCH'])
def update_incicent_comment(id):
    try:
  
        data = request.get_json()
        comment = data.get('comment')
        
        if len(Incident.incidents) == 0:
            return jsonify({
                'message': 'There are no incident yet!',
                'status': 404
            }), 404
        incident = Incident.incidents[id-1]
        for incident in Incident.incidents:
            if incident["id"] == id:
                incident['comment'] = comment

        return jsonify({
                'status': 200,
                'data': incident,
                'message': 'update'
            })
    except IndexError:
        return jsonify({
            'message': 'incident does not exit or check your id',
            'status': 404
        }), 404


@app.route('/api/v1/delete_incident/<int:id>', methods=['GET'])
def delete_incicent(id):
    try:
        if len(Incident.incidents) == 0:
            return jsonify({
                'message': 'There are no incident yet!',
                'status': 404
            }), 404
        incident = Incident.incidents[id-1]
        Incident.incidents.remove(incident)
        return jsonify({
            'status': 200,
            'Data': incident,
            'message': 'incident deleted'
        })
    except IndexError:
        return jsonify({
            'message': 'incident does not exit or check your id'
        }), 404





@app.route('/api/v1/signUp/', methods=['POST'])
def signUp():

    try: 
        data = request.get_json()
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        othername = data.get('othername')
        email = data.get('email')
        phoneNumber = data.get('phoneNumber')
        username = data.get('username')
        registered = data.get('registered')
        password = data.get('password')
        id = len(User.accounts)+1
        isadmin = False

        account = User(firstname, lastname, othername, email,\
         phoneNumber, username, registered, password, id, isadmin)

        
        if account.validate_firstname() is False:
            return jsonify({
                'message': 'Firstname field can not be left empty'
            }), 400
        if account.validate_lastname() is False:
            return jsonify({
                'message': 'Lastname field can not be left empty'
            }), 400
        if account.validate_othername() is False:
            return jsonify({
                'message': 'othername field can not be left empty'
            }), 400
        if account.validate_email() is False:
            return jsonify({
                'message': 'Email field can not be left empty or is invalid(eg: example@example.com)'
            }), 400
        if account.validate_phoneNumber() is False:
            return jsonify({
                'message': 'phoneNumber field can not be left empty and should be more than 9'
            }), 400
        if account.validate_username() is False:
            return jsonify({
                'message': 'Username field can not be left empty'
            }), 400
        if account.validate_registered() is False:
            return jsonify({
                'message': 'Registered field can not be left empty'
            }), 400
        if account.validate_password() is False:
            return jsonify({
                'message': 'Password field can not be left empty or is less than 8'
            }), 400
        
        User.accounts.append(account.__dict__)
        return jsonify({
            'status': 201,
            'account': account.__dict__,
            'message': 'account created'
            }),201
    except Exception:
        return jsonify({'message': 'Something went wrong with your inputs'}), 400


@app.route('/api/v1/accounts/', methods=['GET'])
def get_accounts():
    if len(User.accounts) == 0:
        return jsonify({
            'message': 'There are no user yet!'
        }), 400
    return jsonify({
        'accounts': [account for account in User.accounts]
    }), 200

@app.route('/api/v1/account/<int:id>', methods=['GET'])
def get_single_account(id):
    try:
        if len(User.accounts) == 0:
            return jsonify({
                'message': 'There are no user yet!'
            }), 400
        account = User.accounts[id-1]
        return jsonify({
            'Account': account,
            'message': 'account fetched'
        })
    except IndexError:
        return jsonify({
            'message': 'account does not exit or check your id'
        }), 404





























