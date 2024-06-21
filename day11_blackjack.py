# Blackjack Project
# Patrick Harrold

import random
import os
# Create Deck
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \\  /|K /\\  |     | '_ \\| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \\/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\\\
      |  \\/ K|                            _/ |                
      `------'                           |__/     
"""

# Create Hands
usr_hand = []
dlr_hand = []

# Function to deal a card
def deal(hand:list):
    hand.append(random.choice(deck))

# Function to check if hand is over 21. Include logic from Ace.
def score(cards:list):
    total = 0
    # Keep track of the Aces. Remember, we're not limiting how many we could have.
    ace = 0
    for i in cards:
        # Check for an Ace
        if i == 11:
            ace += 1
        total += i
    # Check how many Aces should be a 1 instead and reduce the score as needed.
    for _ in range(ace):
        if total > 21:
            total -= 10
    return total

wins = 0
losses = 0

# Start playing.
blackjack = input("Do you want to play blackjack? 'y' or 'n' ")
while blackjack == 'y': 
    # Deal 2 cards to each player
    print (logo)
    for _ in range(2):
        deal(usr_hand)
        deal(dlr_hand)

    # Show cards to user
    print (f"Your cards: {usr_hand}. Your current score: {score(usr_hand)}.")    
    print (f"The dealer's first card: {dlr_hand[0]}")
    # Hit or stand for the user
    usr_over = False
    hit = 'y'
    while not usr_over and hit == 'y':
        hit = input ("Type 'y' to get another card, type 'n' to pass: ")
        if hit == 'y':
            deal(usr_hand)
            if score(usr_hand) > 21:
                print (f"Your hand is {usr_hand} and your score is {score(usr_hand)}. You are over 21.")
                usr_over = True
            else:
                print (f"Your hand is {usr_hand} and your score is {score(usr_hand)}.")

    # User is done hitting so now we go through the same logic with the dealer. Only go into this if the user didn't go over.
    # He can't stop until he's >= 17.
    dlr_over = False
    while not dlr_over and score(dlr_hand) < 17:
        deal(dlr_hand)
        if score(dlr_hand) > 21:
            dlr_over = True

    # 5 cases: user over, dealer over, user higher than dealer, dealer higher than user, and finally equal scores and a tie.
    usr_score = score(usr_hand)
    dlr_score = score(dlr_hand)
    if not usr_over:
        print (f"Your hand is {usr_hand} and your score is {usr_score}.")
    print (f"The Dealer's hand is {dlr_hand} and his score is {dlr_score}.")

    if not usr_over and not dlr_over:
        if usr_score > dlr_score:
            wins += 1
            print ('''You win!

             ___________
            '._==_==_=_.'
            .-\\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \\::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`
                   ''')
        elif usr_score < dlr_score:
            losses += 1
            print ("You lose!")
        else: # Scores are equal
            print ("It's a tie.")
    elif not usr_over and dlr_over:
        print ("You win!")
    else:
        print ("You lose!")
    blackjack = input("Do you want to play another game of blackjack? 'y' or 'n' ")
    usr_hand = []
    dlr_hand = []
    os.system('clear')