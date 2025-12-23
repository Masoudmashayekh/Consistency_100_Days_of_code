import random
from art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1, True
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1, True
    else:
        print(f"You got it! The answer was {actual_answer}")
        return turns, False
        

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").capitalize()
    if level == "Easy":
        return EASY_LEVEL_TURNS
    elif level == "Hard":
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    actual_answer = random.randint(1,100)
    print(actual_answer)

    turns = set_difficulty()
    game_on = True
    while game_on and turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")  
        user_guess = int(input("Make a guess: "))
        turns, game_on = check_answer(user_guess= user_guess, actual_answer= actual_answer, turns= turns)
        if game_on and turns > 0:
            print("Guess again.")
        elif turns == 0 and game_on:
            print("You've run out of guesses, you lose.")
            game_on = False

        
        
play_again = True
while play_again:      
    game()
    play = input("Do you want to play again? Type 'y' or 'n'. ").capitalize()
    if play == "N":
        print("See you later Good boy!")
        play_again = False