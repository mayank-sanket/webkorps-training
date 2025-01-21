# to count the number of references of a value



import sys

print(sys.getrefcount(24601)) #prints 3
print(sys.getrefcount(123)) #prints 5
print(sys.getrefcount('hi')) # prints 3


# as it can be seen, the reference counts are not real as the number of times these values have been used in the memory is not equal to what we get here || actual way to do so is a bit different

a = 10
a = 'chaiaurcode'
a = 3.14
# print(sys.getrefcount(a))   

# note: in python, the data type is of the value in the memory and not of the variable name

# garbage numbers and strings are not IMMEDIATELY collected by python. They are collected but not immediately (as they might be used immediately -- optimisation)


a = 5
b = 2

a = a + 2\

## an interesting example: 

listA = [1, 2, 3] 
listB = listA
listA[1] = 99
print(listB[1]) # prints 99

# but notice the different behaviour from the above code
myListOne = [1, 2, 3]
myListTwo = myListOne
myListOne = 'chai'
print(myListTwo) # prints [1, 2, 3] 

myListOne = [1, 2, 3]
print(myListTwo) # prints [1, 2, 3]

print(myListOne) # prints [1, 2, 3]

myListOne[0] = 33
print(myListTwo) #prints [1, 2, 3]

#---------
l1 = [1, 2, 3]
l2 = l1
print(l1) # [1, 2, 3]
print(l2) # [1, 2, 3]
l1[0] = 44
print(l2)  # [44, 2, 3]


# all this is related to the concept of reference

# another interesting example:


p1 = [1, 2, 3] 
p2 = p1

p2 = [1, 2, 3] # this [1, 2, 3] has other reference than the first [1, 2, 3]

p1[1] = 99

print(p2[1]) # still prints 2 and not 99 because of the other reference

# -------------------------------------

h1 = [1, 2, 3] 
h2 = h1[0:2]  # slice from zeroth to second index (second not inclusve) 
print(h2)  # [1, 2]

h3 = h1[:]  # no start and end assigned therefore it automatically understands it to be from zeroth element to the last element (both inclusive) 
print(h3) # [1, 2, 3]  but this time it is a copy

h1[0] = 99
print(h1) # [99, 2, 3]
print(h3) # [1, 2, 3]


a1 = [1, 2, 3]
a2 = a1[:]
a1[0] = 90
print(a1)  # [90, 2, 3]
print(a2) # [1, 2, 3]

#note: slice is copy


# other way to copy : longer way

import copy

s1 = [1, 2, 3]
s2 = copy.copy(s1) #notice

s1[0] = 23
print(s1) # [23, 2, 3]
print(s2) # [1, 2, 3]


r1 = [1, 2, [9, 10], 3]
r2 = copy.copy(r1) #notice

r1[2][0] = 200
print(r1)   # [1, 2, [200, 10], 3]
print(r2)  # [1, 2, [200, 10], 3] ##### IMPORTANT 

# note: if you want this behaviour in 2D list (nested lists) then you have to use deep copy for that otherwise, you will not be able to COPY the reference

c1 = [1, 2, [9, 10], 3]
c2 = copy.deepcopy(c1)  #notice
c1[2][0]  = 101
print(c1) # [1, 2, [101, 10], 3]
print(c2) # [1, 2, [9, 10], 3]   ##IMPORTANT



z1 = [1, 2, [3, 9], 19]
z2 = copy.deepcopy(z1)  #notice

z1[2][1] = 11
print(z1) # [1, 2, [3, 11], 19]
print(z2) # [1, 2, [3, 9], 19]



# an interesting question:

n = [1, 2, 3]
m = n
print(m == n) # true
print(m is n) # true

s = [1, 2, 3]
t = s
t = [1, 2, 3]

print(s == t) # true
print(s is t) # false