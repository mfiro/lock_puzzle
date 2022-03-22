import random
from exceptions import InvalidNumberOfDigitsException

def analyse(guess, secret):
    """Analyses the input and compare it with the solution 
    and returns a clue in form of tuple which indicating
    how many digits are correctly guessed and how many of them
    are also in correct positions.

    :param guess: the number to be compared with the lock code, e.g: "555" (required)
    :type guess: str

    :param secret: the secret lock code, e.g: "345" (required)
    :type secret: str

    returns:
        a tuple (correct, misplaced):
            correct: the number of found digit which is also correctly placed.
            misplaced: the number of found digits which is misplaced.
    
    """

    guess = list(guess)
    secret = list(secret)

    if len(guess) != len(secret):
        raise InvalidNumberOfDigitsException(len(secret))

    correct = 0
    misplaced = 0

    remained_a = guess.copy()
    remained_b = secret.copy()

    for x, y in zip(guess,secret):
        if x == y:
            correct += 1
            remained_a.remove(x)
            remained_b.remove(y)
    
    for x in remained_a:
        if x in remained_b:
            misplaced += 1
            remained_b.remove(x)

    return (correct, misplaced)


def generate_secret(n_digits):
    secret = random.randint(0,10**n_digits-1) # 999 for n_digits = 3
    return f'{secret:{n_digits}d}'


def human_readable_clue(analyse_result):
    """Convert correct, misplaced number to a human readable clue
    """

    if analyse_result == (0, 0):
        return "Nothing is correct"
    else:
        correct, misplaced = analyse_result
        message = f"{correct+misplaced} digit(s) correct: "
        message += f"{correct} in the correct position and {misplaced} wrongly placed"
        return message