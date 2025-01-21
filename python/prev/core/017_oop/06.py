class Car:

    # declare and initialise a variable here
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        

        
        # every time this 'constructor' method is called the value gets updated 
        Car.total_car += 1



class EV(Car):
    def __init__ (self, brand, model, battery_cap):
        super(). __init__(brand, model)
        self.battery_cap = battery_cap


my_tesla = EV('tesla', 'model S', '90kWh')   

my_tata = Car('tata', 'nexon')
my_maruti = Car('maruti suzuki', 'swift dzire')

print(Car.total_car)  # prints 3
print(my_maruti.total_car) # this also prints 3 

# better syntax among these two: Car.total_car



# sometimes the memory is not immediately cleared, therefore sometimes variables are temporarily there for some time for optimisation purpose


# NOTE: you can also creeate objects directly without taking their reference, eg:

Car('a', 'b')
Car('x', 'y')

print(Car.total_car) # prints 5 now