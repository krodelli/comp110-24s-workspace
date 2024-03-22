"""Battleship part two."""

__author__ = "730466512"

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

result_box = RED_BOX if row_guess == secret_row and column_guess == secret_column else WHITE_BOX

row_counter = 1
while row_counter <= grid_size:
    row_string = ""
    column_counter = 1

    if row_counter == row_guess:
        while column_counter <= grid_size:
            if column_counter == column_guess:
                row_string += result_box
            else:
                row_string += BLUE_BOX
            column_counter += 1
    else:
        while column_counter <= grid_size:
            row_string += BLUE_BOX
            column_counter += 1

    print(row_string)
    row_counter += 1

# Part 3: Giving a Hint
# Check if the guess is a hit or miss
if row_guess == secret_row and column_guess == secret_column:
    print("Hit!")
elif row_guess != secret_row and column_guess == secret_column:
    print("Close! Correct column, wrong row.")
elif row_guess == secret_row and column_guess != secret_column:
    print("Close! Correct row, wrong column.")
else:
    print("Miss!")