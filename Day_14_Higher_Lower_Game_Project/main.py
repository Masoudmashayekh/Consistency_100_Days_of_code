from game_data import instagram_data
from art import VS_ART_SIMPLE, HIGH_LOW_ART
import random
def game():
    account_a = random.choice(instagram_data)
    account_b = random.choice(instagram_data)
    while account_a == account_b:
        account_b = random.choice(instagram_data)
    print(HIGH_LOW_ART)
    score = 0
    continue_game = True
    while continue_game:
        print(f"Compare A: {account_a["name"]}, {account_a["description"]}, {account_a["country"]} ")
        print(VS_ART_SIMPLE)
        print(f"Against B: {account_b["name"]}, {account_b["description"]}, {account_b["country"]} ")
        choose = input("Who has more followers? Type 'A' or 'B': ").upper()
        if choose == "q":
            print(f"Your score is {score} .")
            quit()
            
        if choose == "A" and account_a["followers_count"] > account_b["followers_count"]:
            score += 1
            print(f"You're right! Current score: {score}")
            account_b = random.choice(instagram_data)
            while account_a == account_b:
                account_b = random.choice(instagram_data)
        elif choose == "B" and account_b["followers_count"] > account_a["followers_count"]:
            score += 1
            print(f"You're right! Current score: {score}")
            account_a = random.choice(instagram_data)
            while account_a == account_b:
                account_a = random.choice(instagram_data)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_game = False
            
game()