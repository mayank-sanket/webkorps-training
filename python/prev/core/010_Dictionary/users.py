
user_data = {
    "mayank": {
        "name": {
            "firstName": "Mayank",
            "lastName": "Sanket"
        },
        'age': 23,  # wrote 23 intensionally as compared to '21' in priyank, to check some properties
        'currentLocation':{
            "city": "Madhepura",
            "state": "Bihar",
            "country": "India"
        },
        "isLoggedIn": {
            'status': True,
            'lastLoggedInAt': 'Bihar'
        }
    },

    "priyank":{
        "name": {
            "firstName": "Priyank",
            "lastName": "Sanket"
        },
        "age": '21',   # wrote '21' intensionally instead of 21 to check some properties 
        "currentLocation": {
            "city": "Noida",
            "state": "Uttar Pradesh",
            "country": "India"
        },
        'isLoggedIn': {
            'status': False,
            'lastLoggedInAt' : 'Delhi'
        }
    }
}


print(user_data['mayank']['currentLocation']['state'])  # Bihar

priyank_age = user_data['priyank']['age']         # 21
print(priyank_age) # 21
print(type(priyank_age))   # <class 'str'>
# print(priyank_age + 1) # error

print((int(priyank_age)) + 1)  # 22

