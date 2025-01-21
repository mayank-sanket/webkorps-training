# a file has an iter tool of its own, lists etc don't have their own iter tool by default
# eg: in a list: 
# list = [1, 2, 3]
# i = iter(list)


# in file
# f = open('file.txt')
# iter(f)   # here you don't need to store iter in a variable


# try doing this:
# print(iter(f) is f)    # True    


# print(iter(f) is f.__iter__()) # True  | prints True for file only and not for other iterables like Lists, etc.

# mynewList = [1, 23,]
# print(iter(mynewList) is mynewList)     # False


# do this in  terminal

# f = open('chai.py')

# f.readline() # repeat this line till you start getting empty string '' in the terminal 


# this shows that the file is iterable
# using the readline() method, you can also read all the comments written in the code file or any text file as it reads line by line

# now do this in the terminal:
 
# f.__next__()    # it would give 'import time\n' in the console  | the readline() method internally uses it but the readline() method does some more tasks and makes things easier for you

# if you keep printing f.__next__() in the terminal, you willl get this at the end:    File "<stdin>", line 1 in <module> StopIteration


# easy way to use the __next__() method: use loops

# for line in open('chai.py').readline():  # cosumes more memory to run
#     print(line)      # prints characters line by line  



# for line in open('chai.py'):  #  consumes less memory
#     print(line)     # prints each line individually

# or do this

# while(True):
#     line = f.readline()
#     if not line: break
#     print(line, end= '')    



# --------------------------------- an example -------------
test = 'mayank'
if not test: 
    print('chai')     
# --------------------------------------------


# NEW ------------

myList = [1, 2, 3, 4]
i = iter(myList)          # the reference of the iter of an iterable object can be stored in a variable
print(i)  # <list_iterator object at 0x0000022E1D074C70>

print(i.__next__()) # prints 1  # if you repeat this step, it will print 2 and if you keep repeating, it will print till 4 but after that you will get 'StopIteration' and an error in the terminal



# DICTIONARY is also iterable
D = {'a': 1, 'b': 2}
for key in D.keys():
    print(key)  # prints a b in new lines

J = iter(D)
print(J)  # <dict_keyiterator object at 0x0000028FAC85DA30>
print(J.__next__())    # prints a
print(J.__next__())  # prints b


# NOTE: you can also write J.__next__() as next(J)
# print(J.__next__())  # error | StopIteration




# RANGE

print(range(5)) # range(0, 5)
r = range(0, 5)


K = iter(r)
print(K) # <range_iterator object at 0x000001D30D88AEF0>

print(K.__next__()) # 0
print(K.__next__()) # 1
print(K.__next__()) # 2                || or this syntax: print(next(K))
print(K.__next__()) # 3
print(K.__next__()) # 4 
# print(K.__next__()) # Error | StopIteration



# Note the assignment to variable I in upper part could also be changed to iter(r) or any other iterables |