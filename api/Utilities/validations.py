from api.Models.Users import User
import re
import os
class Validations:
    '''Class handles all user validations when signup'''
    def user_validation(self, firstname, lastname, othernames, email, phone_number, username, password):
        '''method that validate all the user inputs'''
        if not firstname or firstname == "" or not type(firstname) == str:
            return {
                'status': 400,
                'error': 'Firstname field can not be left empty and should be a string'
            }

        if not lastname or lastname == "" or not type(lastname) == str:
            return {
                'status': 400,
                'error': 'Lastname field can not be left empty and should be a string'
            }
        
        if not othernames or othernames == "" or not type(othernames) == str:
            return {
                'status': 400,
                'error': 'othernames field can not be left empty and should be a string'
            }
     
        if not email or not type(email) == str or email == "" or \
        not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", email):
            return {
                'status': 400,
                'error': 'Email field can not be left empty, is invalid(eg: example@example.com) and should be a string'
            }
        
        if not phone_number or phone_number == "" or not type(phone_number) == str:
            return {
                'status': 400,
                'error': 'phone_number field can not be left empty and should be a string!'
            }
        
        if not username or username == "" or not type(username) == str:
            return {
                'status': 400,
                'error': 'Username field can not be left empty and should be a string'
            }
 
        if not password or password == "" or not type(password) == str:
            return {
                'status': 400,
                'error': 'Password field can not be left empty and should be a string'
            }
        
    @staticmethod
    def empty_user(data):
        ''' Function enables to check if the accounts list is empty
        :param:
        data - holds information of the accounts list in the User class
        :returns:
        a error message.
        '''
        if len(data) == 0:
            return {
                'status': 404,
                'error': 'There are no user yet!'
            }

    @staticmethod
    def validate_signup(username, email):
        ''' Function enables to check if the user exist in the account list
        :param:
        username - holds the username entered by a user and check if it matches any username in the accounts list
        email - holds the email entered by a user and check if it matches any email in the accounts list
        both :returns:
        a error message.
        '''

        for user in User.accounts:
            if user["username"] == username:
                return {
                    'status': 409,
                    'error': 'username already taken'
                }
            elif user["email"] == email:
                return {
                    'status': 409,
                    'error': 'email already existed'
                }

class Login_validation:
    '''Class handles all user validations when login'''
    def exist_user_validation(self, username, password):
        '''method that validate all the login input from the user'''
        if not username or username == "" or not type(username) == str:
            return {
                'status': 400,
                'error': 'Username field can not be left empty and should be a string'
            }

        if not password or password == "" or not type(password) == str:
            return {
                'status': 400,
                'error': 'Password field can not be left empty and should be a string'
            }

class Incident_validation:
    '''Class handles all incident validations'''
    def add_incident_validation(self, createdBy, incType, location, status, image, video, comment):
        '''Method that validate all the incident input from the user'''
        if not createdBy or not isinstance(createdBy, int):
            return {
                'status': 400,
                'error': 'createdBy field can not be left empty and should be an integer'
                }

        if not incType or incType == "" or not incType == "intervention" \
        and not incType == "red-flag" or not isinstance(incType, str):
            return {
                'status': 400,
                'error': 'incType field can not be left empty, it should be eg: red-flag or intervention\
                and should be a string'
            }
    
        if not location or location == "" or not isinstance(location, str):
            return {
                'status': 400,
                'error': 'location field can not be left empty and should be a string'
            }
    
        if not status or status == "" or not status == "draft" \
        and not status == "under_investigation" and not status== "rejected"\
         and not status=="resolved" or not isinstance(status, str):
            return {
                'status': 400,
                'error':'status field can not be left empty, it should be eg: draft, resolved, under_investigation or rejected \
                and should be a string'
            }
        extensions = [".jpg", ".png"]
        details = os.path.splitext(image)
        if details[1] not in extensions:
            return {
                'status': 400,
                'error': 'image has an invalid format(eg: image.png  or image.jpg'
            }
        extensions = [".mp4", ".avi"]
        details = os.path.splitext(video)
        if details[1] not in extensions:
            return {
                'status': 400,
                'error': 'video has an invalid format(eg: video.mp4  or video.avi)'
        }

        if not comment or comment == "" or not isinstance(comment, str):
            return {
                'status': 400,
                'error': 'comment field can not be left empty and should be a string'
            }
    
    @staticmethod
    def empty_incident(data):
        ''' Function enables to check if the reports list is empty
        :param:
        data - holds information of the reports list in the User class
        :returns:
        a error message.
        '''
        if len(data) == 0:
            return {
                'status': 400,
                'error': 'There are no incident yet!'
            }

    @staticmethod
    def validate_red_flag_comment(comment):
        ''' Function enables to validate comment
        :param:
        comment - holds the comment information entered by a user before update it
        :returns:
        a error message.
        '''
        if not comment or comment == "" or not isinstance(comment, str) :
            return {
                'status': 400,
                'error': 'comment field can not be left empty and should be a string'
            }
            
    @staticmethod
    def validate_red_flag_location(location):
        ''' Function enables to validate location
        :param:
        location - holds the location information entered by a user before update it
        :returns:
        a error message.
        '''
        if not location or location == "" or not isinstance(location, str):
            return {
                'status': 400,
                'error': 'location field can not be left empty and should be a string'
            }
