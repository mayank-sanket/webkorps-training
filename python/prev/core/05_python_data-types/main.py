print(12+12) # 24
print(2.5*5) #12.5

print(2**100) # 1267650600228229401496703205376

import math
print(math.pi) # 3.141592653589793

import random
print (random.random()) # 0.8312907054890533 or any random number  



print(random.choice([1, 2, 3, 4, 5, 6])) # any random number from this array


username = "mayank"
print(len(username)) # 6

print(username[1]) # a
print(username[-1]) # k

# username[0] = 's'  

 ## TypeError: 'str' object does not support item assignment (because string is immutable)


print(username[1:3]) # starting index 1, ending index (not included)=> ay


#a useful thing: dir(variable)   || to take help related to methods


print(dir(username))



# ------------------------------------------------

myList = [123, "hi", 1.121]
print(myList)
print(len(myList))
print(myList[1])
print(myList[-1]) 


# ______________________________

location = "New Delhi"
myDict = {"name":"mayank", "age": 22, "location": location}

print(myDict['name']) #name

# ----------------------------------

myTup = (1, 2, 4)
print(myTup[1])  #2
len(myTup)
