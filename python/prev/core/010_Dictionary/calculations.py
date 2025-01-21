squared_nums = {x: x**2 for x in range(5)}   # {0: 0, 1: 1, 2: 4, 3: 9, .... 4:16}

print(squared_nums[4]) # 16

cube_no = {x: x**3 for x in range(1, 11)} # {1:1, 2: 4, 3: 9, ... .. 10: 1000}
print(cube_no[10]) # 1000
print(cube_no) # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}




# SOME METHODS

squared_nums.clear()
print(squared_nums) # {}


# an interesting thing 

keys = ['masala', 'ginger', 'lemon']
default_value = "Delicious"

new_dict = dict.fromkeys(keys, default_value)

print(new_dict)  # {'masala': 'Delicious', 'ginger': 'Delicious', 'lemon': 'Delicious'}


# 
# dict2  = dict.fromkeys(keys, keys) 
# print(dict2) #  {'masala': ['masala', 'ginger', 'lemon'], 'ginger': ['masala', 'ginger', 'lemon'], 'lemon': ['masala', 'ginger', 'lemon']}