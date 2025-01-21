tea_varieties = ["Black", "Green", "Oolong", "White"]
print(tea_varieties) # in list format

print(tea_varieties[0], tea_varieties[1], tea_varieties[-1]) # individual elements

print(tea_varieties[0:2]) # 0th index and 1st index
print(tea_varieties[:3]) # 0th index to 2nd index
print(tea_varieties[1:])  # 1st index to the last index
print(tea_varieties[:])   # all the indexes


tea_varieties[2] = "Herbal" 
print(tea_varieties[2]) # Herbal

# tea_varieties[3:4] = "Lemon"  # not recommended
# print(tea_varieties[3]) # L only

list = ['zero', 'one', 'two', 'three']

list[0:1] = 'hello'
print(list[0])  # h
print(list[0:]) # ['h', 'e', 'l', 'l', 'o', 'one', 'two', 'three']


list[1:2] = "world"

print(list[0:]) # ['h', 'w', 'o', 'r', 'l', 'd', 'l', 'l', 'o', 'one', 'two', 'three']
print(list) # ['h', 'w', 'o', 'r', 'l', 'd', 'l', 'l', 'o', 'one', 'two', 'three']

# problematic

lst = ['one', 'two', 'three', 'four']
print(lst[1:2])  # ['two']

lst[1:2] = 'test'
print(lst[1:2])  # ['t']

print(lst) # ['one', 't', 'e', 's', 't', 'three', 'four']

# how to prevent the above problem? ans: pass a a list

print("-----------------------")
newlst = ['one', 'two', 'three', 'four']
print(newlst[1:2]) # ['two']
newlst[1:2] = ['test']
print(newlst[1:2]) # ['two']

print(newlst) # ['one', 'test', 'three', 'four']

# question:

someList = ['black', 'green', 'oolong', 'white']
print(someList[1:3]) # ['green', 'oolong']
someList[1:3] = ['a', 'b']
print(someList) # ['black', 'a', 'b', 'white']
print(someList[1:3]) # ['a', 'b']

#------------------------------------------

#question:

print(someList[1:1]) # []  | empty array

# what if
someList[1:1] = ['test', 'test']
print(someList) # ['black', 'test', 'test', 'a', 'b', 'white']

someList[2:2] = ['alpha', 'alpha', 'alpha', 'alpha']
print(someList) # ['black', 'test', 'alpha', 'alpha', 'alpha', 'alpha', 'test', 'a', 'b', 'white']


# question:

anotherList = ['green', 'white', 'black', 'white']
print(anotherList[1:2]) # ['white']
print(anotherList[1:3]) # ['white', 'black']

anotherList[1:3] = []
print(anotherList) # ['green', 'white']

#-----------------------------------------------------------------

# LOOPS

for item in anotherList:
    print(item)

for item in anotherList:
    print(item, end=' ')    # prints in the same line separated by space

print('\n')

for item in anotherList:
    print(item, end=', ')    # prints in the same line separated by comma
print('\n')




# CONDITIONALS

if "blue" in anotherList:
    print('Yes, blue exists!')    




if "green" in anotherList:
    print('Green found')
else:
    print('green not found')


if "pink" in anotherList:
    print('pink found')
elif "white" in anotherList:
    print('white found')
else:
    print('no color found')   


# some methods:

# APPEND

anotherList.append('purple')     

print(anotherList)

# POP
anotherList.pop() # removes the last element

#REMOVE
anotherList.remove('green')
print(anotherList)

# INSERT

anotherList.insert(1, 'green')
print(anotherList) 

anotherList_copy = anotherList
anotherList[0] = "TEST"
print(anotherList_copy)  # ['TEST', 'green']


# what if you don't want to copy the original reference?
# ans: since list is mutable by default, therefore the original reference is passed but if you don't want it
#  use the .copy() method

newAnotherListCopy = anotherList.copy()
anotherList[0] = "COPY"
print(newAnotherListCopy) # ['TEST', 'green']

# QUESTION:
newAnotherListCopy.append('aquamarine')
print(newAnotherListCopy)
print(anotherList) # change is not reflected here
