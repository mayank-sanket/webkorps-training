class Car:
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model

    


class Battery:
    def battery_info(self):
        return "this is battery"
        


class Engine:
    def engine_info(self):
        return "this is engine"



# Class ElectricCarTwo inherits from 3 classes namely Battery, Engine and Car class

class ElectricCarTwo(Battery, Engine, Car):
    pass

myNewTesla = ElectricCarTwo('Tesla', "Model S")

print(myNewTesla.engine_info())
print(myNewTesla.battery_info())