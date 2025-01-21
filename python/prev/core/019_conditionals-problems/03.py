score = int(input('enter score: '))


if score > 100:
    print('Please enter a valid score.')
    exit() # to exit the program without going further

    
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B" 

elif score >= 70:
    grade = "C"

elif score >= 60: 
    grade = "D"

else:
    grade = "F"

print("grade:",grade)    