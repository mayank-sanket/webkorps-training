# BASIC FUNCTION SYNTAX:



def square_of_num(num):
    square = num ** 2
    print(square)

square_of_num(12) # prints 144

zyx = square_of_num(6)   # prints 36 |||| IMPORTANT TO OBSERVE

print(zyx) # prints None   | because there is no return in the definition



# another definition:

def sq (num):
    square = num**2
    return square

sq(10) # does not print anything
print(sq(10)) # prints 100

res = sq(10)
print(res) #  prints 100
