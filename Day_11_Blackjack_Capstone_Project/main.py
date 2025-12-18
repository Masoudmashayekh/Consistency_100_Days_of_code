# Day_11 Blackjack Capstone Project
import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

my_cards = []
pc_cards = []
for _ in range(2) :
    my_cards.append(cards[random.randint(0, len(cards)-1)])
    pc_cards.append(cards[random.randint(0, len(cards)-1)])
    
print(f"Your cards: {my_cards}")
print