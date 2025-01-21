class Car:
    brand = None
    model = None


my_car = Car()
print(my_car) # <__main__.Car object at 0x00000276EF985880>

his_car = Car()
print(his_car) # <__main__.Car object at 0x000001A36F715E50>


# in the above syntax, you cannot pass arguments (if you try, you will get an error)


# class Vaahan:
#     def __init__(usermodel, userbrand):
#         brand = userbrand
#         model = usermodel

# my_vaahan = Vaahan('renault', 'duster')    
# print(my_vaahan.brand)
# print(my_vaahan.model)    



# in the above syntax, there is no communication between the attributes 'brand', 'model' and the class 'Vaahan', therefore you will get an error while doing : print(my_vaahan.brand)

# we need to have the conncection, and for that connection, we need to use the self keyword



class Gaadi:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

meri_Gaadi = Gaadi('Toyota', 'Corolla')


print(meri_Gaadi.brand) # Toyota
 
print(meri_Gaadi.model) # Corolla


uski_Gaadi = Gaadi('maruti suzuki', 'alto')

print(uski_Gaadi.brand) # maruti suzuki
print(uski_Gaadi.model) # alto

print(meri_Gaadi.brand)  # Toyota
print(meri_Gaadi.model)  # Corolla