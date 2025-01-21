# List is mutable
# a similar data type was needed which functions like a tuple but is immutable


tea_types = ('black', 'green', 'oolong')
print(tea_types) # ('black', 'green', 'oolong')

print(tea_types[1]) # green
print(tea_types[-1]) # oolong
print(tea_types[0:])
print(tea_types[0:2])
print(tea_types[2:3])
print(tea_types[:])


# since tuple is immutable, you cannot change the values assigned to the indexes

# tea_types[0] = 'lemon'
# print(tea_types[0])


# but you can re-assign the entire variable like this:    | In immutables, you can change the memory reference but cannot change the individual values 

# tea_types = (1, 2, 3) 
# print(tea_types)     # THIS IS VALID

# SOME METHODS:

print(len(tea_types)) # 3



# -----------------------
more_tea = ('herbal', 'earl grey')
all_tea = more_tea + tea_types

print(all_tea) # ('herbal', 'earl grey', 'black', 'green', 'oolong')

if 'herbal' in all_tea:
    print('yes, herbal found')

#  --------------------------

# methods contd:
some_tea = ('herbal', 'lemon', 'herbal', 'green', 'herbal')
print(some_tea.count('herbal'))  # 3
print(some_tea.count('mayank'))   # 0


# some other things: THE CONCEPT OF UNPACKING (similar to destructuring in JavaScript)

tup = ('Black', 'Green', 'Oolong')

(black, green, oolong) = tup
print(black)  # Black

(green, black, oolong) = tup
print(green)   # Black   | corresponding sequence

# (oolong, green, black, white) = tup # error  =>  ValueError: not enough values to unpack (expected 4, got 3)
# print(white)     # error: ValueError: not enough values to unpack (expected 4, got 3)

print(type(tup)) # <class 'tuple'>



# NESTED TUPLE:

tup1 = (1, 2, (99, 110), 4, 5, (11, 22))
print(tup1[2][1]) # 110