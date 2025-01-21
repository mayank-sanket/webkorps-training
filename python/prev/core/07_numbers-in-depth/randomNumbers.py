import random


print(random.random()) # any random number b/w 0 (inclusive) and 1(exclusive)



print(random.choice([1, 2, 3, 4, 5, 6]))



choiceList = [1, 32, 11, 23]
print(random.choice(choiceList))


print(random.randint(0, 100)) # random no. b/w 0 and 100 (included)



choiceList2 = ['lemon', 'masala', 'ginger', 'mint']
print(random.choice(choiceList2))


random.shuffle(choiceList)
print(choiceList) # list gets printed in a shuffled manner
