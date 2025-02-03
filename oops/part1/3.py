class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def sayHiToUser(self, user):
        print(f"Sending message to {user.username}: Hi {user.username}!, It's {self.username}")


user1 = User('alexhales', 'alexhales@gmail.com', 'alex@234')
user2 = User('brettlee', 'brettlee@gmail.com', 'brett234')
user3 = User('coreyanderson', 'coreyander@gmai.com', 'corey454')


user1.sayHiToUser(user2) # Sending message to brettlee: Hi brettlee! It's alex hales

print(user1.email) # alexhales@gmail.com
user1.email = "joeroot@gmail.com"

print(user1.email) # joeroot@gmail.com