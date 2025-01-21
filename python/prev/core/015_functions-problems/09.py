
# Generator Function with yield
##   Write a generator function that yields even numbers up to a specified limit

# general way:

def even_generator(limit):
    for i in range(2, limit+1, 2):      # last parameter is called 'step', we passed 2 here because in python, the last argument is not inclusive
        print(i)

even_generator(12)         # 2 4 6 8 10 12 (in new lines)

# question: 
def ev_gen(lim):
    for i in range(2, lim, 2):
        return i

print(ev_gen(10)) # prints 2 only because the function returns after 2 

# Note: to prevent such things we use a different keyword called 'yield'

# 'yield' also returns value but also keeps it in the memory alongwith its state




# other solution to above question:

def even_gen(lim):
    myList = []
    for i in range(2, lim , 2):
        myList.append(i)
    return myList

print(even_gen(12)) # prints [2, 4, 6, 8, 10, 12]         but in list format and we don't want in list format, we want directly


print("-----------------------------")













# SOLUTION SOLUTION SOLUTION

def even_genr(limit):
    for i in range(2, limit+1, 2):
        yield i


for num in even_genr(12):
    print(num)     # prints 2 4 6 8 10 12 in new lines






















# note: the syntax for num in abc(x):      does not work with functions where yield keyword is not used
#  eg:

# def somefxn(lim):
#     for i in range(2, lim + 1, 2):
#         return i
    
# for num in somefxn(12):
#     print(num)    # TypeError: 'int' object is not iterable