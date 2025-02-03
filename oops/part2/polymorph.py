

class Car:
    def __init__(self, brand, model, year, num_of_doors, num_of_wheels):
        self.brand = brand,
        self.model = model,
        self.year = year
        self.num_of_doors = num_of_doors
        self.num_of_wheels = num_of_wheels

    def start(self):
        print('Car starting ...')

    def stop(self):
        print('Car stopping ...')


class Bike:
    def __init__(self, brand, model, year, num_of_wheels):
        self.brand = brand,
        self.model = model,
        self.year = year,
        self.num_of_wheels = num_of_wheels

    def start(self):
        print('Bike starting ...')

    def stop(self):
        print('Bike stopping ...')





# car.start()
# bike.stop()


# ___________________________________________________________________________________

# creating a list of Vehicles to inspect

vehicles = [
    Car("Hyundai", 'Creta', 2016, 5, 4),
    Car('Maruti', 'Alto', 2014, 5, 4),
    Bike('Hero', 'Glamour', 2011, 2)
]

# loop through the list of vehicles and inspect them

for vehicle in vehicles:
    # vehicle.start()
    # vehicle.stop()



    # if isinstance (vehicle, Car):
    #     print('Hurray! Car starting ...')
    # if  isinstance(vehicle, Bike):
    #     print('Yo! Bike starting ...')


    if isinstance(vehicle, Car):
        print(f"Inspecting  {vehicle.brand} {vehicle.model} {vehicle} {type(vehicle).__name__}")
        vehicle.start()
        vehicle.stop()

    elif isinstance(vehicle, Bike):
        print(f"Inspecting {vehicle.brand} {vehicle.model} {vehicle} {type(vehicle).__name__} ")
        
    else:
        raise Exception ('The object is not a valid vehicle.')
    