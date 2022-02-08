def analyse(a, b):
    """Analyses the input and compare it with the solution and returns a clue in form of tuplewhich indicating how many digits are correctly guessed and how many of them are also in correct positions.

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

