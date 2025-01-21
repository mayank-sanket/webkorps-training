class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + ' is the best brand in the world!'
    
    def getFullName(self):
        return f'{self.__brand} {self.model}'
    
    def fuel_type(self):
        return "Petrol or Diesel"
    

class ElectricCar(Car):
    def __init__ (self, brand, model, battery_capacity):
        super(). __init__ (brand, model)
        self.battery_capacity = battery_capacity

    def fuel_type(self):   # same method name with differeent return types
        return "Electric Charge"        

my_tesla = ElectricCar("Tesla", "Model S", '90kWh')



print(my_tesla.getFullName())   # Tesla Model S  | note that we had not privatised the getFullName method



# ---------------------------------------
print(my_tesla.fuel_type())  # Electric Charge

my_swift = Car('Maruti Suzuki', "Swift Dzire")

print(my_swift.fuel_type()) # Petrol or Diesel

