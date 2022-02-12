from analyse import analyse, human_readable_clue, generate_code


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
        print(f"Failed! -> The lock code was {solution}")


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
        response = input("Play again? [Y/n] ")
        if response.lower() != 'y':
            play_game = False
        














