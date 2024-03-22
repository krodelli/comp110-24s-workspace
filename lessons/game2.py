from random import randint

SECRET: int = randint(1,10)
correct: bool = False

while correct == False: #not correct
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"You got it right! {guess} is the secret number")
        correct = True 
    else:
        if guess < SECRET:
            print("too low, try again")
        if guess > SECRET:
            print("too high, try again")