import math

def circlemeasurements (radius):
    area = math.pi*radius**2
    circumference = math.pi*2*radius

    return {'area': area, 'circumference': circumference } # dictionary is being returned

res = circlemeasurements(7)
print('Area: ', round(res.get('area'), 4))
print('Circumference: ', round(res.get('circumference'), 4))


# or 

def calc(rad):
    area = math.pi*rad**2
    circumference = math.pi*2*rad
    return area, circumference

print(calc(7)) # prints area and circumference  in tuple

# similarly you could have returned list or tuple also



# or 
def fxn(rad):
    area = math.pi*rad**2
    circumference = math.pi*2*rad
    return area, circumference

a, c = fxn(7)
print('Area: ', a)
print('Circumference: ', c)

