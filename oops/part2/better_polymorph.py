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


    def start(self):
        print('Car is starting...')
   
    def stop(self):
        print('Car is stopping')

class Bike(Vehicle):
    def __init__(self, brand, model, year, num_of_wheels):
        super().__init__(brand, model, year)
        self.num_of_wheels = num_of_wheels

    def start(self):
        print('bike is starting') # over-writing the parent class method
        
    def stop(self):
        print('bike is stopping')


# creating a list of Vehicles to inspect

vehicles = [
    Car("Hyundai", 'Creta', 2016, 5, 4),
    Car('Maruti', 'Alto', 2014, 5, 4),
    Bike('Hero', 'Glamour', 2011, 2)
]

# loop through the list of vehicles and inspect them (better syntax as we don't have to manually change start, stop as per conditions)

for vehicle in vehicles:
    if isinstance(vehicle, Vehicle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})"  )
        vehicle.start()
        vehicle.stop()
    else:
        raise Exception ('Object is not a valid vehicle')
    



# note (this type of syntax is alos valid (linting))
# vehicles: list[Vehicle] = [
#     Car("Hyundai", 'Creta', 2016, 5, 4),
#     Car('Maruti', 'Alto', 2014, 5, 4),
#     Bike('Hero', 'Glamour', 2011, 2)
# ]