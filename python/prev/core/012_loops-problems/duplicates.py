#  A list has two or more items which are duplicate. Your task is to find those items and store them in a new list uniquely

list = ['apple', 'banana', 'orange', 'apple', 'mango', 'mango', 'apple']

newList = []

for item in list:
    if(list.count(item)>1):
        print(item)
        break

for item in list:
    if(item in newList): 
        continue
    if(list.count(item) > 1):
        newList.append(item) 
    

print(newList)