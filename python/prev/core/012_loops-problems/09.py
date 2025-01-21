
items = ['apple', 'banana', 'orange', 'apple', 'mango']


# my solution:

for item in items:
    if items.count(item) > 1:
        print(item)
        print('the list has duplicate items')




# hitesh sir's solution to the first problem

unique_item = set()

for item in items:
    if item in unique_item:
        print("DUPLICATE: ", item)
        break
    unique_item.add(item)