import random
from analyse import analyse

def generate_puzzle():
    solution = random.randint(0,999)
    return f'{solution:03d}'


def human_readable_clue(correct, misplaced):
    return (correct, misplaced)


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

    solution = generate_puzzle()

    max_attempt = 5
    n_attempt = 1

    while n_attempt <= max_attempt:
        guess = input(f"\n Attempt {n_attempt} What is your guess? -> ")
        correct, misplaced = analyse(guess, solution)

        if (correct, misplaced) == (3, 0):
            print("Congrats, you have opened the box")
            break
        else:
            clue_message = human_readable_clue(correct, misplaced)
            print(clue_message)
        
        n_attempt += 1

    else:
        print("Failed!")














