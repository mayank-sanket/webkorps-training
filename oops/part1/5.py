# getter and setter


from datetime import datetime
class User:

    def __init__(self, username, email, password):
        self.username = username
        self._email = email 
        self.__password = password   

    

    def get_email(self):
            print(f"Email accessed at {datetime.now()}") # optional (just to notify about time)
            return self._email
    
    def set_email(self, new_email):
         print(f"User email changed to: {new_email} at {datetime.now()}") # optional (just to notify)
         self._email = new_email
    

user1 = User('alexhales', 'alexHALES@gmail.com', 'alex@234')
user2 = User('brettlee', 'brettlee@gmail.com', 'brett234')
user3 = User('coreyanderson', 'coreyander@gmai.com', 'corey454')



# print(user1._email) # prints email but should not do like this
print(user1.get_email())  # correct way

# user1._email = "fakeemail@gmail.com" # works but should not do like this

user1.set_email("changedemail@gmai.com")

print(user1.get_email()) # prints "changedemail@gmail.com"

