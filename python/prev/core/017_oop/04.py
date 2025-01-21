# a private method can be accessed anywhere inside the class but it cannot be DIRECTLY accessed in an object of class 

# to do so, we need getters


# is there a concept of setters? if yes, study about it 

class Car:
    def __init__(self, brand, model):
        self.__brand = brand   # by using two underscores, we made it private within the class => this means the object cannot access it directly without using a getter method
        self.model = model

    def get_brand(self):
        return self.__brand + "!"   # here we can return brand in the way we want it to be returned
    
    def fullName(self):
        return f"{self.brand} {self.model} "
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super(). __init__(brand, model)
        self.battery_capacity = battery_capacity

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# print(my_tesla.brand)
# print(my_tesla.model)
# print(my_tesla.fullName())
# print(my_tesla.battery_capacity)


# ------------------------
print(my_tesla.get_brand())
