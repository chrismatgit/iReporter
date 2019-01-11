from flask import Flask, jsonify, Blueprint
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from api.Controllers.user_controller import signup, login


bp = Blueprint('application', __name__)

@bp.route('/')
def test_route():
    '''Function returns a welcome message'''
    return "welcome to iReporter"

@bp.route('/signup/', methods=['POST'])
def signUp():
    '''Function adds the user to accounts list
    returns a success message and the user details'''
    response = signup()
    return response

@bp.route('/login/', methods=['POST']) 
def user_login():
    response = login()
    return response

@bp.errorhandler(404)
def page_not_found(e):
    return jsonify({
        'issue': 'you have entered an unknown URL',
        'message': 'Please contact us for more details'
    })