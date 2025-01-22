class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullName(self):
        return f"{self.brand} {self.model}"


class ElectricCar (Car):
     def __init__(self, brand, model, battery_size):  # here, brand and models are just placeholders
         super(). __init__(brand, model) # access to the __init__ method from the parent class 
         self.battery_size = battery_size


myElectric_car = ElectricCar('Tesla', 'model S', '85kWh')
print(myElectric_car.battery_size)
print(myElectric_car.brand)
print(myElectric_car.model)
print(myElectric_car.fullName())# this is also accessible


# you could also give brand and model manually but that makes no sense as we are using the property of inheritance

         
# class EV(Car):
#     def __init__ (self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self. price = price


# myEv = EV('a', 'b', 1000)
# print(myEv.price)                 