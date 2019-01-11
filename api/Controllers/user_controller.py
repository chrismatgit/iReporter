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
        validator = Validations(firstname, lastname, othernames, email, phone_number, username, password)
        invalid_firstname = validator.validate_firstname()
        invalid_lastname = validator.validate_lastname()
        invalid_othernames = validator.validate_othernames()
        invalid_email = validator.validate_email()
        invalid_username = validator.validate_username()
        invalid_phone_number = validator.validate_phone_number()
        invalid_password = validator.validate_password()
        valid = Validations.validate_signup(username,email)

        if not valid:
            if not invalid_firstname:
                if not invalid_lastname:
                    if not invalid_othernames:
                        if not invalid_email:
                            if not invalid_phone_number:
                                if not invalid_username:
                                    if not invalid_password:
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
                                    return jsonify(invalid_password), 400
                                return jsonify(invalid_username), 400
                            return jsonify(invalid_phone_number), 400
                        return jsonify(invalid_email), 400
                    return jsonify(invalid_othernames), 400
                return jsonify(invalid_lastname), 400
            return jsonify(invalid_firstname), 400
        return jsonify(valid), 400

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
        validator = Login_validation(username, password)
        invalid_username = validator.validate_username()
        invalid_password = validator.validate_password()
        valid = Validations.empty_user(User.accounts)

        if not valid:
            if not invalid_username:
                if not invalid_password:
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
                return jsonify(invalid_password), 400
            return jsonify(invalid_username), 400
        return jsonify(valid), 400
    except Exception:
        return jsonify({
            'status': 400,
            'error': 'Something went wrong with your inputs'
        }), 400

