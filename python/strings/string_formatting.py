age = int(input('enter your age: '))
salary = int(input('enter your salary: '))


# earlier syntax: .format()

# F-String (python 3.6 onwards) | use of placeholders and modifiers

print(f"Your age is {age}.") 
print(f"Your salary is {salary:.2f}") # modifier  | converts into decimal value with 2 decimal places

# or
decSal = f"Your salary is {format(salary, '.2f')}"
print(decSal)


# 
price = 59000
txtres = f"The price is {price:,} dollars"
print(txtres)

# multiple formatters, such as :b  :> :+    etc (w3schools) | refer for more details



# performing operations in placeholders

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)


# -----------------------------------------


# OLDER SYNTAX (before python 3.6)

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

txt = "The price is {:.2f} dollars"


print(txt.format(price))

# for multiple values

testxt = "hey {} hi {} hehehe {}"
print(testxt.format('mayank', 'test', 'john'));


# INDEX Numbers

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))


# if you want to refer to the same value more than once, use the index number

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))


# Named Indexes

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(model = "Mustang", carname = "Ford")) # order does not matter


tsttxt = "I have a {carname}, it is a {model}".format(model = "Swfit Dzire", carname = "Maruti Suzuki")
print(tsttxt)