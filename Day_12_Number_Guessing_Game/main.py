import random
from art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer, turn):
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



play_again = True
print(logo)
print("Welcome to Number Guessing Game!")
while play_again:
    print("I'm thinking of a number between 1 and 100.")
    actual_answer = random.randint(1,100)
    print(actual_answer)

    level = input("Choose a difficulty. Type 'easy' or 'hard': ").capitalize()
    if level == "Easy":
        turns = EASY_LEVEL_TURNS
    elif level == "Hard":
        turns = HARD_LEVEL_TURNS
    else:
        print("You type wrong input!!!")
    while i > 0:    
        print(f"You have {i} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        check_answer(user_guess= user_guess, actual_answer= actual_answer, turn= i)
    play = input("Do you want to play again? Type 'y' or 'n'. ").capitalize()
    if play == "N":
        play_again = False
        print("See you later Good boy!")