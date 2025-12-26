from game_data import instagram_data
from art import VS_ART_SIMPLE, HIGH_LOW_ART
import random

a = instagram_data[random.randint(0, len(instagram_data)-1)]
b = instagram_data[random.randint(0, len(instagram_data)-1)]


print(f"Compare A: {a["name"]}, {a["description"]}, {a["country"]} ")
print(f"Against B: {b["name"]}, {b["description"]}, {b["country"]} ")
print("Who has more followers? Type 'A' or 'B': ")
score = 0
if a["followers_count"] > b["followers_count"]:
    score += 1
# print("Sorry, that's wrong. Final score: 0")
# print("You're right! Current score: 1")