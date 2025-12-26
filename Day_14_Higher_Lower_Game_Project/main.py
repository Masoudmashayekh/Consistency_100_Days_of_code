# Higher and Lower game project
from game_data import instagram_data
from art import VS_ART_SIMPLE, HIGH_LOW_ART
import random

def format_data(account):
    '''Takes the account data and returns the printable format.'''
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, form {account_country}"


def game():
    account_a = random.choice(instagram_data)
    account_b = random.choice(instagram_data)
    while account_a == account_b:
        account_b = random.choice(instagram_data)
    print(HIGH_LOW_ART)
    score = 0
    continue_game = True
    while continue_game:
        print(f"Compare A: {format_data(account_a)}")
        print(VS_ART_SIMPLE)
        print(f"Against B: {format_data(account_b)}")
        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        if user_guess == "Q":
            print(f"Your score is {score} .")
            quit()
            
        if user_guess == "A" and account_a["followers_count"] > account_b["followers_count"]:
            score += 1
            print(f"You're right! Current score: {score}")
            account_b = random.choice(instagram_data)
            while account_a == account_b:
                account_b = random.choice(instagram_data)
        elif user_guess == "B" and account_b["followers_count"] > account_a["followers_count"]:
            score += 1
            print(f"You're right! Current score: {score}")
            account_a = random.choice(instagram_data)
            while account_a == account_b:
                account_a = random.choice(instagram_data)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_game = False
            
game()