# Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum


# note: if you don't use *, then you cannot pass multiple arguments while using the function

def sum_all(*args):
    return sum(args)  # sum is a built-in method in python


print(sum_all(1, 2)) # 3

print(sum_all(1, 2, 3, 4, 5)) # 15

print(sum_all(3, 7, 10))   # 20


def calc(*something):     # you can use any term name but it should have a * before it 
    return sum(something)

print(calc(10, 20, 30)) # 60



## QUESTION: how would you do this, without using *args 

### by using a list parameter and then looping through the list

def sum_all_lst(somelist):
    res = 0
    for i in somelist:
        res += i
    return res

print(sum_all_lst([1, 2, 3, 89]))  # 95




# --------------------------------------

# what do you get when you try to print *args

def somefxn(*tst):
    print(*tst)
    # return sum(tst)

somefxn(1, 2, 4, 5) # prints 1, 2, 4, 5 in the console 
somefxn(1, 10, 2) #  # prints 1, 10, 2 in the console


def anotherfxn(*tst):
    print(tst)
    return sum(tst)

print(anotherfxn(1, 2, 4))   # prints (1, 2, 4) in one line and 7 in new line


print(anotherfxn(90, 10))  # prints (90, 10) in one line and 100 in another



def otherfxn(*tst):
    print(*tst)
    print(tst)
    return sum(tst)

print(otherfxn(1, 10, 11)) # prints 1, 10, 11 ; (1, 10, 11) ; 22 in 3 different lines

print(otherfxn(1, 4)) # prints 1, 4   ; (1, 4)  ;  5 in 3 different lines


# NOTE: as you can observe, you get tuple when you try to print args, this means args is iterable


def testing(*test):
    sum = 0
    for i in test:
        sum +=i
    return sum

    

# print(testing([1, 2, 3, 4])) # error
print(testing(1, 3, 3)) # 7

def tsting(*tst):
    for i in tst:
        print(2,' X ', i,  ' = ', i*2)


tsting(1, 2, 3, 4, 5, 6, 7)        