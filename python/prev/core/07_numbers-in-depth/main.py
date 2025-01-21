x = 2
y = 3
z = 4
print(x + y)
print(x**y) # 8

print(x + y * z)  # generally this type of syntax is avoided in production level code  => better to use brackets   || however, remember this: PEMDAS => ans = 14

print((x+y)*z) # 20

print(40 + 2.31) # 42.31

# better:
print(40.00 + 2.31) # take care of precision

print(int(30 + 2.1)) # 32
print(float(40)) # 40.0
print(float(2.89)) # 2.89


# ___________________
# operator overloading (based on data type)

print('chai' + 'code') # chaicode

print(x, y, z) # 2 3 4

print(x+1, y+4, z-2) # 3 7 2

print(3%2) # 1
print(2 ** 3) #8
print(100 ** 2 ) # 10000
print(2**1000)  # 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376  

# most of the languages fail to deal with such large numbers 


print(1/3.0) # 0.3333333333333333
print()



#  INTERESTING : => read more from docs

print(repr('chai')) # 'chai'
print(str('chai')) # chai
print('chai') # chai

#-----------------------


print(1<2) # True

print(5 == 5.0) # True
print(5 is 5.0)  # False

print((4 != 5)) # True  

p, q, r = 3, 4, 5
print(p<q<r) # True  (not a good practice to use this syntax) 
# better syntax
print(p<q and q<r) # True

print(1==2 < 3) # False 

#EXPLANATION:  1 == 2 and 2<3 => False and  True => False

