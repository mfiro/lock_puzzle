from game import generate_code
from analyse import analyse

solution = generate_code()

first_guess = generate_code() # just a random attempt

if analyse(first_guess, solution) == (3, 0):
    print(f'Code is cracked. The solution is {first_guess}')

elif analyse(first_guess, solution) == (0, 0):
    pass

else:
    pass

