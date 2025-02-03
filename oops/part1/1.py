class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
    
    def bark(self):
        print('Woof Woof!')

class Owner:
    def __init__(self, name, address, contact_number ):
        self.name = name
        self.address = address
        self.phone_number = contact_number

owner1 = Owner("John", "Indore", "+91 9267893805")
owner2 = Owner('Jack', "Bhopal", "+91 7050270707")

dog1 = Dog("Bruce", "Scottish Terrier", owner1)
dog1.bark()

print(dog1.name) # Bruce

print(dog1.owner.name) # John


dog2 = Dog("Freya", "Greyhound", owner2)
# dog2.bark()
print(dog2.breed) # Greyhound


  