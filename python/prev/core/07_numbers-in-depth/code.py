import math

print(math.floor(3.8))  # 3
print(math.floor(-3.9)) # -4

print(math.ceil(2.7)) # 3
print(math.ceil(2.4)) # 3


# towards zero (trunc)
print(math.trunc(2.8)) # 2
print(math.trunc(-2.8)) # -2


#note:
print(2**200) # 1606938044258990275541962092341162602522202993782792835301376

# but
print(99999999999999999999999 * 2.1) # 2.0999999999999998e+23

# we'll learn to handle this later



#complex numbers:
print((2 + 3j)*3) # 6+9j   

#---------------------------

#OCTAL NUMBERS
print(0o20) #16

#HEXADECIMAL NUMBERS
print(0xFF) # 255

#BINARY NUMBERS
print(0b101) # 5


#CONVERSION OF NUMBERS

print(oct(64)) # prints '0o100'

#similarly, hex, bin

#or any format to decimal
print(int(0b101)) # 5
print(int(0xFF)) #255

# any format to decimal

print(int('64', 8)) #  52  (64 in octal is equal to 52 in decimal)
print(int('64', 16)) # 100
print(int('1000', 2)) # 8


#----------------------

x = 10
print(x<<2) # 40

x = 10
print(x>>1) # 5
print(x>>2) # 2


y = 10
y = y<<2
print(y) # 40

z = 10
z<<=2
print(z) # 40