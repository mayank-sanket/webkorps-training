

print(range(10))  # range(0, 10)    | 0 to 10 (10 exclusive)

y = range(10)
print(y)  # range(0, 10)

# LIST COMPREHENSION

squared_num = [x**2 for x in range(10)]
print(squared_num) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

multiplied_num = [x**2 for x in range(11)] 
print(multiplied_num) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


resultantNumbers = [x+5 for x in range(1, 11)] 
print(resultantNumbers) # [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

cube_num = [y**3 for y in range(1, 5)]
print(cube_num) # [1, 8, 27, 64]