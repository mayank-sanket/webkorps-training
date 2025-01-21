class Car:
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model

class EV(Car):
    def __init__(self, brand, model, battery_capacity):
        super(). __init__(brand, model)
        self.battery_capacity = battery_capacity

my_car = Car("Maruti Suzuki", "Swift Dzire")
elon_car = EV("Tesla", "Model S", "90kWh")

print(isinstance(my_car, Car)) # True
print(isinstance(elon_car, Car)) # True
print(isinstance(elon_car, EV)) # True
print(isinstance(my_car, EV))  # False