# Prime Number Checker

num = 20
is_Prime = True

if num > 1:
    for i in range(2, num):
        if(num%i == 0):
            is_Prime = False
            break

if(is_Prime):
    print('Prime')
else:
    print('Not prime')



# using the function syntax:

def isPrime(n):
    if n<=1:
        return False
    else:
        for i in range(2, n):
            if(n%i)==0:
                return False
        return True      



print(isPrime(2))
print(isPrime(6))



# or (notice the synatx where the last return statement is written)

def isprime(n):
    if n<=1:
        return False
    else:
        for i in range(2, n):
            if(n%i) == 0:
                return False
    return True


print(isprime(22))
print(isprime(7))