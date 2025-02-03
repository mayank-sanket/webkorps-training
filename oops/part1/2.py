class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} old.")


mayank = Person('Mayank', 23)
sanket = Person('Sanket', 20)

mayank.greet()
sanket.greet()

elon = Person(name = 'Elon', age = 30) # valid
elon.greet()