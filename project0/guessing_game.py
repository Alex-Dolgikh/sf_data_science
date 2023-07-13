import numpy as np


def guess_game(number: int=1) -> int:
    """Алгоритм угадывает число от 1 до 100
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    counter = 0
    upper = 101
    lower = 0
    while True:
        counter += 1
        guess_number = np.random.randint(lower, upper) 
        if guess_number < number:
            lower = guess_number + 1
        elif guess_number > number:
            upper = guess_number
        else: 
            break 
        
    return counter

def score_game(guess_game) -> int:
    """ За какое количество попыток в среднем за 10000 подходов 
        алгоритм угадывает загаданное число.

    Args:
        guess_game (function): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    counter_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(10000))

    for number in random_array:
        counter_ls.append(guess_game(number))

    score = int(np.mean(counter_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    
if __name__ == '__main__':
    print('Run benchmarking for game: ', end='')
    print(score_game(guess_game))