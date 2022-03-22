from utils import analyse, human_readable_clue, generate_secret


def game(n_digits=3):
    secret = generate_secret(n_digits)
    print(f'Secret code generated : {"*"*n_digits}')
    max_attempt = 7
    n_attempt = 1

    while n_attempt <= max_attempt:
        guess = input(f"\n Attempt {n_attempt} What is your guess? -> ")

        try:
            correct, misplaced = analyse(guess, secret)
        except Exception as e:
            print(e.message)
            continue

        if guess == secret:
            print("Congrats! you have opened the box ^--^")
            break
        else:
            clue_message = human_readable_clue((correct, misplaced))
            print(clue_message)
        
        n_attempt += 1

    else:
        print(f"Failed! -> Secret code was {secret}")


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

    play_game = True
    n_digits = input("How many digits should the lock have? ")
    n_digits = int(n_digits)

    while play_game:
        game(n_digits)
        response = input("Play again? [Y/n] ")

        if response.lower() != 'y':
            play_game = False
        else:
            n_digits = input("How many digits should the lock have? ")
            n_digits = int(n_digits)
