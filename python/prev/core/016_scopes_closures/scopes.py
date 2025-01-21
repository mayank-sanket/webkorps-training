# scopes are also called namespaces

username = "mayank-sanket"

def fun():
    username = "chai"
    print('local variable: ', username)  # to print this, you need to call the function 'fun'

fun()   

print('global variable: ', username) 


def fun2():
    print('GLOBAL: ', username) # because there is no local variable called username in the scope
fun2()





# note: inside a particular scope, the priority of local variable is more than the global one     || bottom to top approach






x = 99 # in global scope

def fun3(y):
    z = x + y
    return z
result = fun3(1)

print(result)  # 100

def fun4():
    x = 88      # this x is local

print(x) # 99 (global scope)    





def fun5():
    global x
    x = 12
fun5()  # this step is necessary, otherwise the line below will print the global value of the variable x, which is 99
print(x) # 12 because we used the global keyword in fun5 


# the syntax in fun5 has nothing wrong in it, but it is not recommended to modify global variables from inside a local scope because it can create confusion in large code-bases



# ------------------------------------------------

y = 98

def f6():
    y = 1000
    def f61():
        print(y)   # 1000 | it has access to the variable in the parent function
    f61() # calling function f61 by the function f6 and calling f6 in the global scope is necessary to print 100 in the above code
f6()      

# but what if the parent fxn does not have a variable y: in this case, the inner function accesses the value of y from the outermost (here global) scope

def f7():
    def f71():
        print(y)  # prints 98
    f71()
f7()            

