from game_data import instagram_data
from art import VS_ART_SIMPLE, HIGH_LOW_ART
import random

a = instagram_data[random.randint(0, len(instagram_data)-1)]
b = instagram_data[random.randint(0, len(instagram_data)-1)]

score = 0
continue_game = True
while continue_game:
    print(f"Compare A: {a["name"]}, {a["description"]}, {a["country"]} ")
    print(f"Against B: {b["name"]}, {b["description"]}, {b["country"]} ")
    print("Who has more followers? Type 'A' or 'B': ")

    if a["followers_count"] > b["followers_count"]:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        
    