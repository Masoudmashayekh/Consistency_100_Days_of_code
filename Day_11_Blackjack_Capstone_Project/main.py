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

    
def compare(u_score, p_score):
    if u_score == p_score:
        return "Draw 🙄"
    elif p_score == 0:
        return "Lose, Opponent has Blackjack 😰"
    elif u_score == 0:
        return "Win with a Blackjack 🤭"
    elif u_score > 21 and p_score > 21:
        return "Draw 😬"
    elif u_score > 21:
        return "You went over. You lose 😢"
    elif p_score > 21:
        return "Opponent went over. You win! 🥇"
    elif u_score > p_score:
        return "You win! 🥇"
    else:
        return "You lose 😡"
    
            
def play_game():
    is_game_over = False
    user_cards = []
    pc_cards = []
    user_score = -1
    pc_score = -1

    for _ in range(2) :
        user_cards.append(deal_card())
        pc_cards.append(deal_card())
    
    
    while not is_game_over:   
        user_score = calculate_score(user_cards)
        pc_score = calculate_score(pc_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {pc_cards[0]}")


        if user_score == 0 or pc_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
                
    while pc_score != 0 and pc_score < 17:
        pc_cards.append(deal_card())
        pc_score = calculate_score(pc_cards)
    
    

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {pc_cards}, final score: {pc_score}")
    print(compare(u_score= user_score, p_score= pc_score))
    
    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" *20)
    play_game()