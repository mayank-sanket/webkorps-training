password = input('Password: ')

length = len(password)

if length<6:
    strength = 'weak'

elif length <= 10: 
    strength = "medium"

else: 
    strength = "strong"

print(f'password is {strength}.') 