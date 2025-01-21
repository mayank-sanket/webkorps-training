# Write a function that greets a user. If no name is provided, it should greeet with a default name


def greet(name = 'mayank'): 
    return "Hello, " + name + "!"

print(greet()) #n prints hello mayank! as the default parameter has value of 'mayank'

print(greet('sanket')) # prints hello sanket!