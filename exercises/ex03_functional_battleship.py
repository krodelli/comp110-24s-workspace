"""Battleship part three."""
__author__ = "730466512"
import random 

# part one defining input guess function.


def input_guess(grid_size: int, guess_row_or_column: str) -> int:
    """Function to prompt user to guess row or column within the gridsize."""
    assert guess_row_or_column == "row" or guess_row_or_column == "column"  # error if neither "row" or "column".
    
    guess = int(input(f"Guess a {guess_row_or_column}: "))
    while guess < 1 or guess > grid_size:
        print(f"The grid is only {grid_size} by {grid_size}. Try again: ")
        guess = int(input(f"Guess a {guess_row_or_column}: "))
    return guess

# part two defining print grid function. 


def print_grid(grid_size: int, row_guess: int, column_guess: int, correct: bool) -> None:
    """Function to print grid with guess and determine the correctness."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"

    row_counter: int = 1  # initalize row counter. 
    while row_counter <= grid_size:  # loop through each row. 
        column_counter: int = 1  # initalize column for current row. 
        row_string = ""  # initalize column counter for current row.  
        while column_counter <= grid_size:  # is current position within the grid.  
            if row_counter == row_guess and column_counter == column_guess and correct:
                row_string += RED_BOX  # if guessed correctly red box. 
            elif row_counter == row_guess and column_counter == column_guess and not correct:
                row_string += WHITE_BOX  # if guessed incorrectly white box.
            else:
                row_string += BLUE_BOX
            column_counter += 1
        print(row_string)  # print the row string representing the current row.
        row_counter += 1  # move to next row. 

# part three defining correct guess function. 


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Determining if the guess is correct."""
    if secret_row == row_guess and secret_column == column_guess:
        return True  # you hit the ship
    else:
        return False

# part four defining main function.


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Starts other functions, runs game."""
    num_turns: int = 0  # initalize the number of turns.
    
    while num_turns < 5:
        print(f"=== Turn {num_turns + 1}/5 ===")  # printing current number of the turn.
        
        row_guess: int = input_guess(grid_size, "row")
        column_guess: int = input_guess(grid_size, "column")
       
        correct = correct_guess(secret_row, secret_column, row_guess, column_guess)
        
        print_grid(grid_size, row_guess, column_guess, correct)  # print the grid with the user's guess and if it is correct or not.
        
        if correct:  # if guess is correct, the game ends, and they won the game.
            print(f"Hit! You won in {num_turns + 1}/5 turns!")
            return
        
        num_turns += 1
        
    print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))