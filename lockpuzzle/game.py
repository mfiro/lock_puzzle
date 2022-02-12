import random
from analyse import analyse

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


def game():

    solution = generate_code()
    max_attempt = 5
    n_attempt = 1

    while n_attempt <= max_attempt:
        guess = input(f"\n Attempt {n_attempt} What is your guess? -> ")
        correct, misplaced = analyse(guess, solution)

        if (correct, misplaced) == (3, 0):
            print("Congrats, you have opened the box")
            break
        else:
            clue_message = human_readable_clue((correct, misplaced))
            print(clue_message)
        
        n_attempt += 1

    else:
        print("Failed!")


if __name__ == "__main__":
    init_message = """
    Welcome!
    This puzzle includes a box which is locked by a three digit combination lock!
    You have 5 attempts to find the solution.
    After each attempt, you'll get a clue which helps you.

    Let's begin
    """
    print(init_message)
    print(f"{'-'*100}")

    solution = generate_code()

    play_game = True
    while play_game:
        game()
        response = input("Play again? [Y/n]")
        if response.lower() != 'y':
            play_game = False
        














