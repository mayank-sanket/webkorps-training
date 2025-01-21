# Polymorphism in Functions

# - Write a function multiply that multiplies two numbers, but can also accept and multiply two strings
# eg: 5*5 should return 25 but 'm' * 5 should return 'mmmmm'


# CASE 1: when you don't get input from user and use hard-coded values

def mult(x, y):
    return(x * y)

print(mult(2, 34)) # 68
print(mult(3, 'n')) # nnn
print(mult('m', 4)) # mmmm




# CASE 2: when you get the input from users | by default the input is treated as string

def multiply_inputs(input1, input2):
    try:
        # Case 1: Both inputs are numbers (multiply them)
        if input1.isdigit() and input2.isdigit():
            return int(input1) * int(input2)
        
        # Case 2: First input is a number, second is a string
        elif input1.isdigit():
            return input2 * int(input1)

        # Case 3: First input is a string, second is a number
        elif input2.isdigit():
            return input1 * int(input2)
        
        # Case 4: If both inputs are strings, multiplication doesn't make sense
        else:
            return "Cannot multiply two strings!"
    
    except ValueError:
        return "Invalid input for multiplication!"
    


# Get inputs from the user
input1 = input("Enter the first input: ")
input2 = input("Enter the second input: ")

# Call the function and print the result
result = multiply_inputs(input1, input2)
print("Result:", result)




# -------------------------------------------------













# 
# NOTE: 
# x = input('enter x')
# y = input('enter y')
# print(type(x), type(y)) # this will print <class 'str'> 
# print(x+y)  # concatenates the values
# print(x*y) # error