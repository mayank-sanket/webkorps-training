# protected : _
# private : __


class User:

    def __init__(self, username, email, password):
        self.username = username
        self._email = email # protected (you should not try to access it outside this class)
        self.__password = password   # private (cannot access)

    # def get_email(self):
    #     return self._email

    def clean_email(self):
        return self._email.lower().strip()
    
    def get_password(self):
        return self.__password
    

user1 = User('alexhales', 'alexHALES@gmail.com', 'alex@234')
user2 = User('brettlee', 'brettlee@gmail.com', 'brett234')
user3 = User('coreyanderson', 'coreyander@gmai.com', 'corey454')


# print(user1.clean_email())

# user1._email = "testemail@gmail.com"

print(user1.clean_email()) # alexhales@gmail.com
print(user1._email) # alexHALES@gmail.com

user1._email = "testemail"
print(user1._email) # testemail
# print(user1.email) # error

# print(user1.__password) # cannot access private attributes

print(user1._email)

print(user1.get_password()) # alex@234
# print(user1.__password)  # error (due to name mangling by double underscore | under the hood)

