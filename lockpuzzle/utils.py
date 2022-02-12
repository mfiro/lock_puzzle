import random

def analyse(a, b):
    """Analyses the input and compare it with the solution 
    and returns a clue in form of tuple which indicating
    how many digits are correctly guessed and how many of them
    are also in correct positions.

    :param a: the number to be compared with the lock code, e.g: "555" (required)
    :type a: str

    :param b: the reference lock code, e.g: "345" (required)
    :type b: str

    returns:
        a tuple (correct, misplaced):
            correct: the number of found digit which is also correctly placed.
            misplaced: the number of found digits which is misplaced.
    
    """

    a = list(a)
    b = list(b)

    correct = 0
    misplaced = 0

    remained_a = a.copy()
    remained_b = b.copy()

    for x, y in zip(a,b):
        if x == y:
            correct += 1
            remained_a.remove(x)
            remained_b.remove(y)
    
    for x in remained_a:
        if x in remained_b:
            misplaced += 1
            remained_b.remove(x)

    return (correct, misplaced)


def generate_code():
    solution = random.randint(0,999)
    return f'{solution:03d}'


def human_readable_clue(analyse_result):
    """Convert correct, misplaced number to a human readable clue
    
    There are 9 possible tuples:

    (0,0), (0, 1), (0, 2), (0, 3)
    (1, 0), (1, 1), (1, 2)
    (2, 0), (2, 1)
    (3, 0) -> this one is caught earlier, no need to implement it.
    """
    if analyse_result == (0, 0):
        return "Nothing is correct"
    elif analyse_result == (0, 1):
        return "One digit is correct but wrongly placed"
    elif analyse_result == (0, 2):
        return "Two digits are correct but wrongly placed"
    elif analyse_result == (0, 3):
        return "All digits are correct but wrongly placed"

    elif analyse_result == (1, 0):
        return "One digit is correct and well placed"
    elif analyse_result == (1, 1):
        return "Two digits are correct but one of them is wrongly placed"
    elif analyse_result == (1, 2):
        return "All digits are correct but two of them are wrongly placed"

    elif analyse_result == (2, 0):
        return "Two digits are correct and well placed"
    elif analyse_result == (2, 1):
        return "All digits are correct but one of them is wrongly placed"
    else:
        return "N/A"


