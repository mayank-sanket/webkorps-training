
# role based authentication

from datetime import datetime
class User:

    def __init__(self, username, email, password):
        self.username = username
        self._email = email 
        self.__password = password   

    

    def get_email(self):
            print(f"Email accessed at {datetime.now()}") # optional (just to notify about time)
            return self._email
    
    def set_email(self, auth, new_email):
         if auth:
              
              self._email = new_email
              print(f"User email changed to: {new_email} at {datetime.now()}") # optional (just to notify)
         else:
              print('You are not authorized to change the password')
    def get_password(self):
          return self.__password
    
    def auth(self):
         psw = input('Enter the password: ')
         if psw == self.__password: 
              pass # add logic later
            
user1 = User('alexhales', 'alexHALES@gmail.com', 'alex@234')()
user2 = User('brettlee', 'brettlee@gmail.com', 'brett234')
user3 = User('coreyanderson', 'coreyander@gmai.com', 'corey454')


# note : even if an attribute is not there in an object, you can add and view it, like: 
user1.newfield = "hello"
print(user1.newfield) # prints "hello"











