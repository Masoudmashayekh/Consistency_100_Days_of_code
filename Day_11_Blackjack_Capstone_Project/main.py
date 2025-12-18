# Day_11 Blackjack Capstone Project
import random


def test(my_cards,pc_cards):
    my_total = sum(my_cards)
    pc_total = sum(pc_cards)
    print(my_cards)
    print(pc_cards)
    if 21 >= my_total > pc_total:
        print("You win!")
    elif my_total < pc_total or my_total > 21:
        print("You loss!!!")
    else:
        print("Draw!")






cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

my_cards = []
pc_cards = []
for _ in range(2) :
    my_cards.append(cards[random.randint(0, len(cards)-1)])
    pc_cards.append(cards[random.randint(0, len(cards)-1)])
    
print(f"Your cards: {my_cards}")
print(f"Computer's first card: {pc_cards[0]}")
decision = input("Type 'y' to get another card, type 'n' to pass:  ")
if decision == 'y':
    my_cards.append(cards[random.randint(0, len(cards)-1)])
    test(my_cards, pc_cards)
else:
    test(my_cards, pc_cards)
