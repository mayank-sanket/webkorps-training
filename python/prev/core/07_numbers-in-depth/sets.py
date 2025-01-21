setOne = {1, 2, 3}
print(setOne) # {1, 2, 3}
print(setOne)

# INTERSECTION OF SETS

print(setOne & {1, 3, 9}) # {1, 3}

# UNIION OF SETS

print(setOne | {1, 2, 3, 4, 5}) # {1, 2, 3, 4, 5}

# DIFFERENCE OF SETS

print(setOne - {3}) # {1, 2}
print(setOne - {1, 2, 3})    # set()   |it is empty set


# note: an empty set is represented by set() in python and not by {} as the latter is used for dictionary



print(type({}))  # <class 'dict'>
print(type(())) # <class 'tuple'>
print(type(set())) # <class 'set'>

print(type(True)) # <class 'bool'>

print(True == 1) # True
print(True is 1) # False

print(False == 0) # True
print(False is 0) # False


print(True + 10) # 11
print(False + 90) # 90
print(False - 1) # -1

