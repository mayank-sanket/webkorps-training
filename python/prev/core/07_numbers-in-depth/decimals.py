# read more about: Decimal Context Managers

print(0.1 + 0.1) # 0.2
print(0.2 + 0.2) # 0.4  

print(0.1 + 0.1 + 0.1) # 0.30000000000000004

print(0.2 + 0.1)  # 0.30000000000000004
print(0.1 + 0.2)  # 0.30000000000000004


print(0.1 + 0.1 + 0.4) # 0.6000000000000001

print(0.1 * 3) # 0.30000000000000004

# https://chatgpt.com/share/6704b154-dd84-8003-9295-f21a77c8ff86


print((0.1 + 0.1 + 0.1) -0.3)  # 5.551115123125783e-17


print(round(0.1 + 0.1 + 0.1, 10))  # 0.3


import math

print(math.isclose(0.1 + 0.1 + 0.1, 0.3))  # True







# to prevent such things, do this:
from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1')) # prints 0.3