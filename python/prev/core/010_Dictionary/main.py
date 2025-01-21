chai_types = {'masala': 'spicy', 'ginger': 'zesty', 'green': 'mild'}
print(chai_types)  # {'masala': 'spicy', 'ginger': 'zesty', 'green': 'mild'}

print(chai_types['masala'])  # spicy
print(chai_types.get('masala')) # spicy 

# difference in behaviour of .get('key') and ['key']
# print(chai_types['massssssssssssalal']) # error
print(chai_types.get('maaaasaalllala')) # no error | output: None


#--------- 
# Manipulations:
chai_types['masala'] = 'fresh'
print(chai_types) # {'masala': 'fresh', 'ginger': 'zesty', 'green': 'mild'}

# LOOPS IN DICTIONARY (not generally used though)
for tea in chai_types:
    print(tea)   # masala ginger green  | prints only the keys (in new lines)

for chai in chai_types:
    print(chai_types[chai]) # fresh zesty mild | prints the values of keys

for chai in chai_types:
    print(chai, chai_types[chai])  # prints keys alongwith values

# another syntax to use loops in dictionary: convert the dictionary into list by using the .items() method

for key, value in chai_types.items():
    print(key, value)  # key alongwith values


# question:

if 'masala' in chai_types:
    print("I have masala chai")     # prints : I have masala chai


# question2: 
print(len(chai_types)) # 3 because the number of keys is 3


# adding more items in the dictionary:
chai_types['earl grey'] = 'citrus'

print(chai_types)

# POP in dictionary: here you need to pass the key also in the argument

chai_types.pop('earl grey') # removes the key-value pair containing 'earl grey'
print(chai_types)



# POPITEM in dictionary: directly removes the last key-value pair (no need to pass key as argument)

chai_types.popitem() 
print(chai_types)


# DELETING thing from the memory:

del chai_types['masala']
print(chai_types)


# COPYING
chaitypes_copy  = chai_types.copy()
chai_types['random'] = 'random value'

print(chaitypes_copy)
print(chai_types)


# SOMETHING LIKE MATRICES IN DICTIONARY : {{}, {}, {}}

tea_shop = {
    "chai":{"masala": "spicy", "ginger": "zesty"},
    "tea": {"green": "mild", "black": "strong"}
}

print(tea_shop)   #  {'chai': {'masala': 'spicy', 'ginger': 'zesty'}, 'tea': {'green': 'mild', 'black': 'strong'}}

print(tea_shop.get('tea'))  # {'green': 'mild', 'black': 'strong'}
print(tea_shop['tea']) # {'green': 'mild', 'black': 'strong'}


print(tea_shop['chai']['masala'])   # spicy
print(tea_shop['tea']['black'])  # strong


# both of these syntaxes work fine
print(tea_shop.get('chai')['masala']) # spicy
print(tea_shop.get('chai').get('masala')) # spicy



# Other Examples:
D = {'a': 1, 'b': 2}



for value in D.items():
    print(value)   # prints ('a', 1) and ('b', 2) in new lines

for key, value in D.items():
    print(key)  # prints a and b in new lines


for key in D.items():
    print(key) # prints ('a', 1) and ('b', 2) in new lines

for k,v in D.items():
    print(k, ": ", v)    # prints a: 1 and b: 2 in new lines