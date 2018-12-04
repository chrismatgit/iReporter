import re
class Validations:
    def __init__(self, firstname, lastname, othername, email, phone_number, username, registered, password):
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.phone_number = phone_number
        self.username = username
        self.registered = registered
        self.password = password
         
    def validate_firstname(self):
        if not self.firstname or self.firstname.isspace() or type(self.firstname) == str:
            return {'message': 'Firstname field can not be left empty'}

    def validate_lastname(self):
        if not self.lastname or self.lastname.isspace() or type(self.lastname) == str:
            return {'message': 'Lastname field can not be left empty'}
        

    def validate_othername(self):
        if not self.othername or self.othername.isspace():
            return {'message': 'othername field can not be left empty'}
        
    
    def validate_email(self):
        if not self.email or self.email.isspace() or \
        not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", self.email):
            return {'message': 'Email field can not be left empty or is invalid(eg: example@example.com)'}
        

    def validate_phoneNumber(self):
        if not self.phone_number or self.phone_number.isspace() or \
        len(self.phone_number)<9:
            return {'message': 'phone_number field can not be left empty and should be more than 9'}
        

    def validate_username(self):
        if not self.username or self.username.isspace():
            return {'message': 'Username field can not be left empty'}
        

    def validate_registered(self):
        if not self.registered or self.registered.isspace():
            return {'message': 'Registered field can not be left empty'}
        
    
    def validate_password(self):
        if not self.password or self.password.isspace() or \
        len(self.password) < 8:
            return {'message': 'Password field can not be left empty or is less than 8'}
        
    # def tearDown(self):
    #     Incident.incidents.clear()

