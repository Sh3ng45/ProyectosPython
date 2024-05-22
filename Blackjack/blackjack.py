############### Blackjack Project #####################

import random
import os
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)

def current_score(cards):
    return sum(cards)

def compare(user_cards, computer_cards):

    '''
    if (current_score(computer_cards) < current_score(user_cards)) and current_score(user_cards) <= 21:
        print("You Win!😄")
        return 0
    '''        
    
    if (current_score(computer_cards) > current_score(user_cards)) and current_score(computer_cards) <= 21:
        print("You Lose🙁")
        return 0

    elif current_score(user_cards) > 21 and current_score(computer_cards) <= 21:
        print("You Lose")
        return 0
    
    elif current_score(computer_cards) > 21 and current_score(user_cards) <= 21:
        print("You Win!😄")
        return 0
    
    elif current_score(computer_cards) == current_score(user_cards):
        print("Draw!")
        return 0
        
    else:
        return


user_cards = []
computer_cards = []
on = False

while len(user_cards) != 2 and len(computer_cards) != 2:
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

play_game = input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()
if play_game == 'y':
    on = True
    os.system('cls')
    print(logo)

while on:

    print(f"Your cards: {user_cards}, current score: {current_score(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    if calculate_score(user_cards) == 0:
        print(f"Your cards: {user_cards}, current score: {current_score(user_cards)}")
        print(f"Computer's final cards: {computer_cards} and his score: {current_score(computer_cards)}")
        print("Blackjack!!")
        on = False
    elif calculate_score(computer_cards) == 0:
        print(f"Your cards: {user_cards}, current score: {current_score(user_cards)}")
        print(f"Computer's final cards: {computer_cards} and his score: {current_score(computer_cards)}")
        print("You Lose, the dealer has a blackjack")
        on = False
    else:
        another = True
        while another and current_score(user_cards) <= 21:
            if current_score(user_cards) > 21:
                print("You Lose")
                on = False
            another_card = input("Type 'y' to get another card. Type 'n' to pass: ").lower()
            if another_card == 'y':
                user_cards.append(deal_card())
                calculate_score(user_cards)
                print(f"Your cards: {user_cards}, current score: {current_score(user_cards)}")
                print(f"Computer's first card: {computer_cards[0]}")

            else:
                another = False
        if current_score(computer_cards) < 17 and current_score(user_cards) <= 21:
            deal = True
            while deal:
                computer_cards.append(deal_card())
                if compare(user_cards, computer_cards) == 0:
                    print(f"Your cards: {user_cards}, current score: {current_score(user_cards)}")
                    print(f"Computer's final cards: {computer_cards} and his score: {current_score(computer_cards)}")
                    deal = False
        else: 
            if compare(user_cards, computer_cards) == 0:
                print(f"Your cards: {user_cards}, current score: {current_score(user_cards)}")
                print(f"Computer's final cards: {computer_cards} and his score: {current_score(computer_cards)}")
            else:
                if (current_score(computer_cards) < current_score(user_cards)) and current_score(user_cards) <= 21:
                    print(f"Your cards: {user_cards}, current score: {current_score(user_cards)}")
                    print(f"Computer's final cards: {computer_cards} and his score: {current_score(computer_cards)}")
                    print("You Win!😄")
        on = False
