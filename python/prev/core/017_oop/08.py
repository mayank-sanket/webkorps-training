class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
    
    @property
    def model(self):
        return self.__model

tata = Car("tata", "safari")

print('----------------------------------')
print(tata.model) # safari 

# since we have the access to the attribute 'model', we can write the value of model again and again

# ----------earlier code without using the @property decorator -----------------

# tata.model = 'tiago'

# print(tata.model) # tiago

# -------------------------------------------



# Now how do we make a property read-only? ans: use a decorator named @property

# now if we try to change the value after object creation, we will get error

# tata.model = 'tiago' # EROROR   | AttributeError: can't set attribute

# print(tata.model())     # ERROR   | TypeError: 'str' object is not callable

# since we used the @property decorator, we can write .model instead of .model() because now it is a property

print(tata.model)  # safari




# importance of @property decorator?
# => if you want to hide a property | not accessible to all
# => if someone wants to acesss the property, then acess through 'my method' for whatever reasons
# => once the property (here brand) is set while creating the instance, it cannot be over-written


