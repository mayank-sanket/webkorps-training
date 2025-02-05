class Vehicle:
    def __init__(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels
        
    
    def start(self):
        print('Vehicle is starting')



class Car(Vehicle):
    def __init__(self, number_of_wheels, number_of_doors):
        super().__init__(number_of_wheels)
        self.number_of_doors = number_of_doors
    
    def start(self):
        print('Car is starting')
    

class Maruti(Car):
    def __init__(self, number_of_wheels, number_of_doors, ai_drive):
        super().__init__(number_of_wheels, number_of_doors)
        self.ai_drive = ai_drive

    def start(self):
        print('Maruti is starting')
    



swift = Maruti(4, 4, False) 

swift.start() # Maruti is starting  | nearest ancestor Class 
print(swift.ai_drive)

