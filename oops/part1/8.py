# static attributes (also known as class attributes)


class User:
    user_count = 0
    def __init__(self, username, email):
        self.username = username
        self.emai = email
        User.user_count +=1

    def display_user(self): # need to verify this
        print(f"Username: {self.username}, Email: {self.email}")
        

user1 = User('mayanksanket', 'mayanksanket@gmail.com')
user2 = User('test', 'test@gmail.com')


print(User.user_count) # 2

print(user1.user_count) # 2  
print(user2.user_count) # 2  