"""Game: guess a number but this time it is machine that guesses! (in 20 or less tries)
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Randomly guessing the number and then narrowing the guess based on whether the number is less or more

    Args:
        number (int, optional): Guessed number. Defaults to 1.

    Returns:
        int: Tries' count
    """
    
    count = 0
    min_num = 1
    max_num = 100
    guess_number = np.random.randint(min_num, max_num) # guessed number
    
    while True:
        count += 1
        mid_num = (max_num + min_num) // 2
       
        if number > mid_num:
            min_num = mid_num
            guess_number = np.random.randint(min_num, max_num) 
        
        elif number < mid_num:
            max_num = mid_num
            guess_number = np.random.randint(min_num, max_num)
        
        else:
            print(f'tries {count}, number {number}')
            break # exiting the cycle
    
    return count


def score_game(random_predict) -> int:
    """Mean number of tries it takes after 10000 iterations for our algorythm

    Args:
        random_predict (_type_): func of guessing

    Returns:
        int: mean number of tries
    """

    count_ls = [] # list of tries' count
    np.random.seed(1) # setting the seed
    random_array = np.random.randint(1, 100, size=(1000)) # guessed a number (10000 times)

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # getiing the mean of tries
    
    print(f'Your algorythm guesses the number in {score} tries on average')
    return score

# RUN
if __name__ == '__main__':
    score_game(random_predict)