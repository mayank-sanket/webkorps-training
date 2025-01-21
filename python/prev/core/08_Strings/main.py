# '', "", """ """

chai =  'Lemon Chai'
print(chai)
chai = 'masala chai'
print(chai)

first_char = chai[0]
print(first_char)  #  same as print(chai[0]) 

slice_chai = chai[0:6] # masala  (6 is exclusive)
print(slice_chai)


numList = "0123456789"
print(numList[:]) # 012345689
print(numList[0:3]) # 012
print(numList[:7]) # 0123456

#IMPORTANT
print(numList[0:7:2]) # 0246
print(numList[0:7:3]) # 036

#=============================

# String Methods
print(chai.lower()) # masala chai
print(chai.upper()) # MASALA CHAI\

print(chai.replace('masala', 'ginger')) # ginger chai


tea = "Lemon, Ginger, Elaichi, Masala, Mint"

print(tea.split(', ')) #  transforms into a list  (comma and space)

print(chai.find("chai")) # 7   | index of the first letter of the string | starting index

print(chai.find('CHAI')) # -1  | because it is not inside the string

paragraph = "Masala chai chai chai chai chai"
print(paragraph.count('chai')) # 5

coffee = "                              black coffee" 
print(coffee.strip()) # black coffee


chai_type = "Masala"
quantity = 2

order = "I ordered {} cups of {} chai"   # {} is called placeholder
print(order) # I ordered {} cups of {} chai\

#but

print(order.format(quantity, chai_type)) # I ordered 2 cups of Masala chai




chai_variety = ['masala', 'lemon', 'ginger', 'elaichi'] 
print(chai_variety) # ['masala', 'lemon', 'ginger', 'elaichi']

print(" ".join(chai_variety)) # masala lemon ginger elaichi
print(", ".join(chai_variety)) # masala, lemon, ginger, elaichi
print("-".join(chai_variety)) # masala-lemon-ginger-elaichi   | useful while creating URLs

print(len(chai_variety)) # 4

someStr = "helloworld"
print(len(someStr)) # 10 

for x in someStr:
    print(x)           # prints the characters of someStr in different lines



statement = "He said, \"Masala Chai is awesome\""  # use of \" \"
print(statement) # He said, "Masala Chai is awesome"

print('Masala\nChai') # Masala 
                      # Chai


# what if you actually want to include the \n also?
# 

print(r'Masala\nChai')                 # Masala\nChai   

t = r'Masala\nChai'   
print(t)

# r stands for raw

#example - windows directory

# directory = r"C:\user\pwd\"   # wrong
 
print("D:\\user\\pwd")   # D:\user\pwd

direct1 = r"C:\user\pwd"   
print(direct1)   # C:\user\pwd

directory2 = r"C:\\user\\pwd"
print(directory2)    # C:\\user\\pwd


#------------------------
testString = "masala chai"

print("masala" in testString) # True
print('mayank' in testString) # False

# read about """ """   (use case to be studied in functions)

