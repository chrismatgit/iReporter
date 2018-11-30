import re
# from api.models import User
class Users_validation:
    def __init__(self, firstname, lastname, othername, email, phoneNumber, username, registered, password, isadmin=False):
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.phoneNumber = phoneNumber
        self.username = username
        self.registered = registered
        self.password = password
        # self.isadmin = isadmin

    def validate_input(self):
        if not self.firstname or self.firstname.isspace():
            return 'Firstname field can not be left empty'
        elif not self.lastname or self.lastname.isspace():
            return 'Lastname field can not be left empty.'
        elif not self.othername or self.othername.isspace():
            return 'Othername field can not be left empty.'
        elif not self.phoneNumber or self.phoneNumber.isspace():
            return 'phoneNumber can not be left empty'
        elif len(self.phoneNumber)<10:
            return 'Phone number has to be longer than 10 characters.'
        elif not self.username or self.username.isspace():
            return 'Username field can not be left empty.'
        elif not self.registered or self.registered.isspace():
            return 'registered can not be left empty'
        # elif not re.match(r"\d{1,2}\/\d{1,2}\/\d{4}+", self.registered)
        #     return 'Enter a valid date... eg: 21/3/2018'
        elif not self.email or self.email.isspace():
            return 'Email field can not be left empty.'
        elif not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", self.email):
            return 'Enter a valid email address.'
        elif not self.password or self.password.isspace():
            return 'Password field can not be left empty.'
        elif len(self.password) < 8:
            return 'Password has to be longer than 8 characters.'
    
    # def check_user_exist(self):
    #     for user in User:
    #         username = user['username']
    #         email = user['email']
    #         if username != None:
    #             return 'Username is taken.'
    #         if email != None:
    #             return 'Email already has an account.'

    # @staticmethod
    # def login_validate(username, password):
    #     if not username or username.isspace():
    #         return 'Username field can not be left empty.'
    #     elif not password or password.isspace():
    #         return 'Password field can not be left empty.'
    #     else:
    #         return False
