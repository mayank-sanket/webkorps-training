class Car:
    def __init__(self, brand, model):
        self.brand= brand
        self.model = model




    # self keyword is necessary to 'create connection' between the method and the class

    def fullName(self):
        return f"{self.brand} {self.model}"
    



mayank_car = Car('Maruti Suzuki', 'Swift Dzire vxi')

print(mayank_car.fullName())