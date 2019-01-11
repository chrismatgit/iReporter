from api.Models.Users import User
import re
import os
class Validations:
    '''Class handles all user validations when signup'''
    def __init__(self, firstname, lastname, othernames, email, phone_number, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phone_number = phone_number
        self.username = username
        self.password = password
    
    def validate_firstname(self):
        '''Method validates the firstname attribute.
        :return:
        a error message
        '''
        if not self.firstname or self.firstname == "" or not type(self.firstname) == str:
            return {
                'status': 400,
                'error': 'Firstname field can not be left empty and should be a string'
            }

    def validate_lastname(self):
        '''Method validates the lastname attribute.
        :return:
        a error message
        '''
        if not self.lastname or self.lastname == "" or not type(self.lastname) == str:
            return {
                'status': 400,
                'error': 'Lastname field can not be left empty and should be a string'
            }
        

    def validate_othernames(self):
        '''Method validates the othernames attribute.
        :return:
        a error message
        '''
        if not self.othernames or self.othernames == "" or not type(self.othernames) == str:
            return {
                'status': 400,
                'error': 'othernames field can not be left empty and should be a string'
            }
        
    
    def validate_email(self):
        '''Method validates the email attribute.
        :return:
        a error message
        '''
        if not self.email or not type(self.email) == str or self.email == "" or \
        not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", self.email):
            return {
                'status': 400,
                'error': 'Email field can not be left empty, is invalid(eg: example@example.com) and should be a string'
            }
        

    def validate_phone_number(self):
        '''Method validates the phone_number attribute.
        :return:
        a error message
        '''
        if not self.phone_number or self.phone_number == "" or not type(self.phone_number) == str:
            return {
                'status': 400,
                'error': 'phone_number field can not be left empty and should be a string!'
            }
        

    def validate_username(self):
        '''Method validates the username attribute.
        :return:
        a error message
        '''
        if not self.username or self.username == "" or not type(self.username) == str:
            return {
                'status': 400,
                'error': 'Username field can not be left empty and should be a string'
            }
    
    def validate_password(self):
        '''Method validates the password attribute.
        :return:
        a error message
        '''
        if not self.password or self.password == "" or not type(self.password) == str:
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
                    'status': 400,
                    'error': 'username already taken'
                }
            elif user["email"] == email:
                return {
                    'status': 400,
                    'error': 'email already existed'
                }
