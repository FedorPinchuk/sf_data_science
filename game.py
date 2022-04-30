"""Game: guess random number"""

import numpy as np

number = np.random.randint(1, 101) # generating a number

count = 0 # tries count

while True:
    count += 1
    guess_number = int(input('Try to guess a number between 1 and 101: '))
    
    if guess_number > number:
        print('Number must be lesser!')
    
    elif guess_number < number:
        print('Number must be bigger!')
    
    else:
        print(f"You've guessed it! The number is {guess_number} in {count} tries!")
        break

