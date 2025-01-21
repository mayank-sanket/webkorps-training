# <details>
# <summary> 10. Pet Food Recommendation
# </summary>
# Recommend a type of pet food based on the pet's species and age (eg. Dog: < 2 years- Puppy food, Cat > 5 years - Senior cat food)
# </details>

pet = input('enter pet: ').lower()
age = int(input('enter age: '))

if pet == 'dog' and age < 2:
    print('puppy food')

elif pet == 'cat'and age > 5: 
    print('senior cat food')