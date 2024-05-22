from art import logo, vs
from game_data import data
import random
import os

# Function to choose a random account from the data
def get_random_account():
    return random.choice(data)

# Function to check if the answer is correct
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "A"
    return guess == "B"

score = 0 # Score counter
on = True # Loop control
optionA = get_random_account() # First account to compare

# Main loop
os.system('cls')
print(logo)
while(on):
    optionB = get_random_account() # Second account to compare
    print(f"Compare A: {optionA['name']}, a {optionA['description']}, from {optionA['country']}")
    print(vs)
    print(f"Against B: {optionB['name']}, a {optionB['description']}, from {optionB['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ").upper() # User input

    # Check if the answer is correct
    if check_answer(answer, optionA['follower_count'], optionB['follower_count']):
        score += 1
        os.system('cls')
        print(logo)
        print(f"You're right! Current score: {score}")
        optionA = optionB
    else:
        os.system('cls')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        on = False
