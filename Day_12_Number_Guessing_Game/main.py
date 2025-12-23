import random
from art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer, turn):
    global turns
    if user_guess > actual_answer:
        print("Too high.")
        turn -= 1
        if turn == 0:
            print("You've run out of guesses, you lose.")
        else:
            print("Guess again.")
    elif user_guess < actual_answer:
        print("Too low.")
        turn -= 1
        if turn == 0:
            print("You've run out of guesses, you lose.")
        else:
            print("Guess again.")  
    else:
        print(f"You got it! The answer was {actual_answer}")
        turn = 0

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").capitalize()
    if level == "Easy":
        return EASY_LEVEL_TURNS
    elif level == "Hard":
        return HARD_LEVEL_TURNS



print(logo)
print("Welcome to Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
actual_answer = random.randint(1,100)
print(actual_answer)

turns = set_difficulty()
print(f"You have {turns} attempts remaining to guess the number.")  
user_guess = int(input("Make a guess: "))
check_answer(user_guess= user_guess, actual_answer= actual_answer, turn= turns)



# play = input("Do you want to play again? Type 'y' or 'n'. ").capitalize()
# print("See you later Good boy!")