# Day_11 Blackjack Capstone Project
import random


def deal_card():
    '''Returns a random card from the deck'''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
    
def calculate_score(cards):
    '''Take a list of cards'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

        
# def test(my_cards,pc_cards):
#     my_total = sum(my_cards)
#     pc_total = sum(pc_cards)
#     print(my_cards)
#     print(pc_cards)
#     if 21 >= my_total > pc_total:
#         print("You win!")
#     elif my_total < pc_total or my_total > 21:
#         print("You loss!!!")
#     else:
#         print("Draw!")


user_cards = []
pc_cards = []
for _ in range(2) :
    user_cards.append(deal_card())
    pc_cards.append(deal_card())
  
    

user_score = calculate_score(user_cards)
pc_score = calculate_score(pc_cards)

print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Computer's first card: {pc_cards[0]}")

