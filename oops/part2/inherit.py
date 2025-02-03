# creating new classes (subclasses or derived classes) based on existing classes (super classes or base classes)

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        print('Vehicle is starting.')

    def stop (self):
        print('Vechicle is stopping')        


class Car(Vehicle):
    def __init__(self, brand, model, year, num_of_doors, num_of_wheels):
        super().__init__(brand, model, year)
        self.num_of_doors = num_of_doors
        self.num_of_wheels = num_of_wheels


class Bike(Vehicle):
    def __init__(self, brand, model, year, num_of_wheels):
        super().__init__(brand, model, year)
        self.num_of_wheels = num_of_wheels



car = Car ('Maruti Suzuki', 'Swift Dzire', 2016, 5, 4)
bike = Bike ('Hero Honda', 'CD Dawn', 2004, 2)

print(car.__dict__) # prints things in dictionary format

print(car.__dir__) # <built-in method __dir__ of Car object at 0x7fc5e7beaf10>

print('hello')