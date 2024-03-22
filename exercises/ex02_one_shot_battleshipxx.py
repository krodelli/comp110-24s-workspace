"""Battleship part two"""

__author__ = "730466512"

# Part 1: Guessing the location
grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

# Prompt the user for a guess
row_guess = int(input("Guess a row: "))
# Check if the guess is within bounds
while not 1 <= row_guess <= grid_size:
    row_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

column_guess = int(input("Guess a column: "))
# Check if the guess is within bounds
while not 1 <= column_guess <= grid_size:
    column_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

# Part 2: Print a Grid
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

row_counter = 1
while row_counter <= grid_size:
    column_counter = 1

    while column_counter <= grid_size:
        if row_counter == row_guess and column_counter == column_guess:
            print(RED_BOX, end="")
        else:
            print(WHITE_BOX if row_counter == secret_row and column_counter == secret_column else BLUE_BOX, end="")
        column_counter += 1

    print()
    row_counter += 1

# Part 3: Giving a Hint
if row_guess != secret_row and column_guess != secret_column:
    if 1 <= row_guess <= grid_size and 1 <= column_guess <= grid_size:
        print("Miss! Correct row, wrong column.")
    else:
        print(f"The grid is only {grid_size} by {grid_size}. Try again: ")

elif row_guess != secret_row:
    print("Miss! Correct column, wrong row.")

elif column_guess != secret_column:
    print("Miss! Correct row, wrong column.")
else:
    print("Hit!")