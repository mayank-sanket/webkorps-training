# Recursive Function
##  Problem: Create a recursive function to calculate the factorial of a number


# recursive fxn syntax: fxn calling itself

def addNum(a, b):
    addNum(2, 1)  # no exit case here



# Syntax 1: 

def factorial(n):
    if(n == 0): return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))    # 120
print(factorial(1)) #  1
print(factorial(0)) # 1 


# Syntax 2: 

def factorialTwo(num):
    if(num == 0): return 1
    return num * factorialTwo(num - 1)   # this syntax also works

print(factorialTwo(6)) # 720 | 