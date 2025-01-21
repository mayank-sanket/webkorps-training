# in the previous question, the 'total_car' variable could be accessed from all the instances of the Car class. 
# but what if you want a method to be accessible for the Class only and not its instances?


# A static method is a method that belongs to a class rather than the instance of the class.
class Car:
    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model


    # use of decorators

    @staticmethod       # if you use this syntax, you don't need to have the 'self' keyword
    def general_description():
        return "Cars are means of transport and are amazing!"

class EV(Car):
    def __init__(self, brand, model, battery_cap):
        super(). __init__(brand, model)
        self.battery_cap = battery_cap

myTesla = EV("Tesla", "Model S", "90kWh")
my_car = Car("Maruti Suzuki", "Swift Dzire")

# print(my_car.general_description()) # this works here (if we use self keyword) but it should not | how to prevent this? use @staticmethod decorator before the method declaration and also remove the 'self' keyword from the declaration


print(Car.general_description())  # here it works if you don't use the self keyword in definition and use @staticmethod decorator  | we don't need to use the self keyword because we are not going to access the method outside the class




# decorators are used in frameworks to implement rules, to enhance functionalities, etc. eg -> 

# @login_required(login_url = 'users.login')

# def show(request):
#     '''
#     Returns the cart index page
#     '''