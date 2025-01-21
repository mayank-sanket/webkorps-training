dist = int(input('distance: '))

if dist <= 3:
    mode = 'walk'
elif dist <= 15:
    mode = 'bike'

else: 
    mode = 'car'




#---------------- AI type response ----------------

if mode == 'walk':
    print(f'AI recommends you to {mode}.')
elif mode == 'bike' or 'car':
    print(f'AI recommends you to use use a {mode}.')    