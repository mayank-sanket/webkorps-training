# using property decorator instead of traditional getter and setter


from datetime import datetime

class User:

    def __init__(self, username, email, password):
        self.username = username
        self._email = email 
        self.__password = password   

    @property
    def email(self):
        print(f'Email accessed at {datetime.now()}')
        return self._email

    @email.setter
    def email(self, newemail):
        # self._email = newemail 
        if "@" in newemail:
            self._email = newemail
        else:
            print("please enter a valid email: ")
        

user1 = User('alexhales', 'alexHALES@gmail.com', 'alex@234')
user2 = User('brettlee', 'brettlee@gmail.com', 'brett234')
user3 = User('coreyanderson', 'coreyander@gmai.com', 'corey454')



print(user1.email) # accessing via the property decorator and not directly (also prints the date and time due to property being used) | notice that we did not do like: print(user1.email())

# print(user1.email()) # error



user1._email = "t@g"
print(user1.email) # t@g #


user1.email = "this@gmail.com" # setting the email (email.setter)
print(user1.email) # getting the email (@property email) # prints: this@gmail.com

 
user1.email = "thisgmail.com"
print(user1.email) # still prints this@gmail.com and also time of accesss |  because the setter could not set due to missing @ in the string




