"""EX01 - Simple Battleship - A cute step towards Battleship."""

__author__ = "730466512"

# part 1 prompting for player 1 input

user_input: str = input("Pick a secret boat location between 1 and 4: ")
user_number: int = int(user_input)

# is user number is less than 1, print error too low, greater than 4 too high  
if user_number < 1: 
    print("Error! " + str(user_number) + " too low!")
    exit()
if user_number > 4: 
    print("Error! " + str(user_number) + " too high!")
    exit()

# part two, prompting for player two input 

second_user_input: str = input("Guess a number between 1 and 4: ") 
second_user_number: int = int(second_user_input)

if second_user_number < 1: 
    print("Error! " + str(second_user_number) + " too low!")
    exit()
if second_user_number > 4: 
    print("Error! " + str(second_user_number) + " too high!")
    exit()

# part 3: checking user input for match 
# if second user number is equal to user number then you hit the ship
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# set the result variable 
if second_user_number == user_number: 
    result: str = RED_BOX 
else:
    result = WHITE_BOX

emoji_string: str = (
    result if second_user_number == 1 else BLUE_BOX) + (
    result if second_user_number == 2 else BLUE_BOX) + (
    result if second_user_number == 3 else BLUE_BOX) + (
    result if second_user_number == 4 else BLUE_BOX)
print(emoji_string)

if second_user_number == user_number: 
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")

