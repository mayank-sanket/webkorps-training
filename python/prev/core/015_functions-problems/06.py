# CREATE A LAMBDA FUNCTION TO COMPUTE THE CUBE OF A FUNCTION

# first have a look at this basic function
def add(a, b):
    return a + b
result = add(12, 39)

# the above kind of function is very helpful if you want to use the functions many times in the code file, but what if you want a function which you won't use that much? here, lambda functions come into the picture


# LAMBDA function

cube = lambda x: x**3   # function without a name but the return value is stored in a variable called cube

print(cube(8)) # 512
print(cube(6)) # 216


print(cube)  # <function <lambda> at 0x000001E15643CFE0>

# other examples:

square = lambda x: x**2
print(square(5)) # 25

sum = lambda x, y: x+y
print(sum(3, 6)) # 9


#NOTE: l
# eg:
calc = lambda x: x+5
calc = lambda x: x+8 # now this  is assigned to the calc variable instead of the former one 
print(calc(5))  # prints 13 and not 10
print(calc)


# use-case of lambdas : in frameworks and libraries