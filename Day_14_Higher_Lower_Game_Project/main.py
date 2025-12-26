from game_data import instagram_data
from art import VS_ART_SIMPLE, HIGH_LOW_ART
import random

A = instagram_data[random.randint(0, len(instagram_data)-1)]
B = instagram_data[random.randint(0, len(instagram_data)-1)]
print(HIGH_LOW_ART)
score = 0
continue_game = True
while continue_game:
    print(f"Compare A: {A["name"]}, {A["description"]}, {A["country"]} ")
    print(VS_ART_SIMPLE)
    print(f"Against B: {B["name"]}, {B["description"]}, {B["country"]} ")
    choose = input("Who has more followers? Type 'A' or 'B': ")

    if choose == "A" and A["followers_count"] > B["followers_count"]:
        score += 1
        print(f"You're right! Current score: {score}")
    elif choose == "B" and B["followers_count"] > A["followers_count"]:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        continue_game = False