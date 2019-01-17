from flask import Flask, jsonify, request
from api.Models.Users import User
from api.Utilities.validations import Validations, Login_validation
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

def signup():
    '''Function creates a new user to the accounts list
    :returns:
    a success message and the user information.
    '''
    try:
        data = request.get_json()
        user_id = len(User.accounts)+1
        firstname = data.get("firstname")
        lastname = data.get("lastname")
        othernames = data.get("othernames")
        email = data.get("email")
        phone_number = data.get("phone_number")
        username = data.get("username")
        password = data.get("password")
        registered = datetime.datetime.now()

        # validations
        validator = Validations()
        invalid_data=validator.user_validation(firstname, lastname, othernames, email, phone_number, username, password)
        valid = Validations.validate_signup(username,email)
        if invalid_data:
            return jsonify(invalid_data), 400

        if not valid:
            password_hash = generate_password_hash(password, method='sha256', salt_length=8)
            account = dict(
                user_id = user_id,
                firstname = firstname,
                lastname = lastname,
                othernames = othernames,
                email = email,
                phone_number = phone_number,
                username = username,
                password = password_hash,
                registered = registered
            )
            User.accounts.append(account)                         
            return jsonify({
                "status": 201,
                "data": account,
                "message": f"{firstname} has been created successfuly"
            }), 201                        
        return jsonify(valid), 409

    except Exception:
        return jsonify({
            'status': 400,
            'error': 'Something went wrong with your inputs'
        }), 400

def login():
    '''Function allows a user to login after sign up
    :returns:
    a success message with the username
    '''
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        validator = Login_validation()
        invalid_data = validator.exist_user_validation(username, password)
        valid = Validations.empty_user(User.accounts)

        if invalid_data:
            return jsonify(invalid_data), 400
        if not valid:
            for user in User.accounts:
                if user["username"]== username and check_password_hash(user["password"],password):
                    token = create_access_token(username)
                    return jsonify({
                        "status": 200,
                        "token": token,
                        "message": f"{username} successfuly login"
                    }), 200
                else:
                    return jsonify({
                        "status": 400,
                        "error": "Wrong username or password"
                    }), 400
        return jsonify(valid), 400
    except Exception:
        return jsonify({
            'status': 400,
            'error': 'Something went wrong with your inputs'
        }), 400


def promote_user_as_admin(user_id):
    '''Function enables an admin to promote a user to be an admin
    :params:
    userd_id - holds integer value of the id of the individual user to be viewed
    :returns:
    a success message and the details of the user whose id matches the one entered by the user
    '''
    try:
        validator = Validations.empty_user(User.accounts)
        if not validator:
            for user in User.accounts:
                if user["user_id"] == user_id:
                    user["isAdmin"] = True
                    return jsonify({
                        "status": 200,
                        "data": user,
                        "message": f"User with user_id {user_id} has been succesfuly promoted as an admin"
                    }), 200
                else:
                    return jsonify({
                        "status": 404,
                        "error": "User does not exist"
                    }), 404
        else:
            return jsonify(validator), 404

    except IndexError:
        return jsonify({
            'message': 'incident does not exit or check your id',
            'status': 404
        }), 404

def get_all_users():
    ''' Function enables the view of all the users
    :returns:
    A list of all the account created
    '''
    validator = Validations.empty_user(User.accounts)
    if not validator:
        return jsonify({
            'status': 200, 
            'Data': [account for account in User.accounts]
        }), 200
    else:
        return jsonify(validator), 404