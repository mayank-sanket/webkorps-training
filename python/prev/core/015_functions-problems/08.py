# Function with **kwargs
# #  Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value


# --------------------------------------------------------------------

# print_kw(name = "shaktiman", power = "laser")

##### A general function with multiple (not variable) number of arguments

def multkw(name, power):
    print("Name:", name, "Power:", power)

multkw(name = "shaktiman", power="laser")  
multkw(power = "laser", name = "shaktiman")  # prints same values in same order
# => you can flip the order of arguments if you have used named arguments



# NOW WHAT IF YOU WANT A FUNCTION WHERE YOU CAN PASS VARIABLE NUMBER OF ARGUMENTS?  

# eg:
# multkw(name = "shaktiman") # error in general function | missing 1 required positional argument: 'power'

# multkw(power= "laser") # error in general function
# multkw(name= "shaktiman", power= "laser") # error in general function

# multkw(name= "shaktiman", enemy = "Dr. Jackaal") # here you will get error | unexpected keyword argument 'enemy'


def printkw(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


printkw(name = 'spiderman', color = 'red', power = 'flying', skill = 'web development')

printkw(name = 'shaktiman', power = 'laser')