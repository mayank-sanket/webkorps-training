# practice more 


x = 12

def fun1():
    x = 99
    def fun2():
        print(x)
    return fun2
myResult = fun1() 
myResult()   # prints 99



def chaicoder(num):
    def acutal_func(x):
        return x ** num
    return acutal_func
result = chaicoder(2)
result2 = chaicoder(3)


print(result) # <function chaicoder.<locals>.acutal_func at 0x00000222D355D1C0>
print(result2) # <function chaicoder.<locals>.acutal_func at 0x00000222D355D260>
 
print(result(3))  # 9
print(result2(3))  # 27