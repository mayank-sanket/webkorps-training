
# My way: 
condition = True

while(condition):
    num = int(input("Enter a number between 1 and 10, both inclusive: \n"))
    if(num >= 1 and num <11):
        # condition = False
        print("Good, now you can leave.\n")
    break
    


      
# Hitesh Sir's way:

while(True):
    number = int(input('Enter a number between 1 and 10: \n '))
    if(1<=number<=10):
        print('Thanks!')
        break
    else:
        print('Invalid number, try again.')

