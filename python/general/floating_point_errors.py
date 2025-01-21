# floating point errors in python

# type 1: 
result = (0.1 + 0.2)
print(result) # prints 0.30000000000000004

# how to avoid? => use round() function
print(round(result, 2)) # 0.3

print(round(result, 3)) # 0.3
print(round(result, 1)) # 0.3
print(round(result, 0)) # 0.0



# or: 

# METHOD 2: use math.isclose() function | rel_tol or abs_tol can be used for relative or absolute tolerance | for loose or strict comparision

import math
print(math.isclose(0.3, result)) # True




# METHOD 3: use Decimal module
from decimal import Decimal

x = Decimal('0.1')
y = Decimal('0.2')

print(x + y) # 0.3


# method 4: use fractions module

from fractions import Fraction

m = Fraction(1, 10)  # 0.1
n = Fraction(2, 10)  # 0.2
p = m + n
print(p)  # 3/10
print(float(p))  # 0.3



# METHOD 5: avoid subtracting close numbers

# Instead of this:
# result = (a - b) + c

# Do this (if mathematically equivalent):
# result = c + (a - b)


# METHOD 6: Scale Values Temporarily

g = 0.1
h = 0.2
i = int(g * 100) + int(h * 100)  # Perform operations in cents
result_in_dollars = i / 100  # Convert back to dollars
print(result_in_dollars)  # 0.3



# METHOD 7: Understand the Error

print(format(0.1 + 0.2, '.25f'))  # Shows the full precision
