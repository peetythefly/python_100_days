import random
import os
# Get the dictionary of elements.
from high_low_data import data
# Get the art
from art import high_low, vs

# Declare the variables.
user_correct = True
score = 0
# Data element example.
    # {
    #     'name': 'Instagram',
    #     'follower_count': 346,
    #     'description': 'Social media platform',
    #     'country': 'United States'
    # },
# Print art.
os.system('clear')
print (high_low)

def show_contender(a_b, contender):
    """Pass in whether it's a or b and the contender. Walks through the logic of properly showing the contender to the user."""
    print(f"Contender {a_b}: {contender["name"]}, {contender["description"]}, from {contender["country"]}.")
# Randomly grab A and print nicely formatted.
contender_a = random.choice(data)
print (f"To help you get started: {contender_a["name"]} has {contender_a['follower_count']} followers.\n")
show_contender("A", contender_a)
correct = True
# Start the loop.
while correct:
    print (vs)
    # Randomly Grab B and print.
    contender_b = random.choice(data)
    # If they are the same get a new contender.
    while contender_a == contender_b:
        contender_b = random.choice(data)
    show_contender("B", contender_b)
    a_fol = contender_a["follower_count"]
    b_fol = contender_b["follower_count"]
    # print (f"Debug. A is {a_fol} and B is {b_fol}.")
    # Get user input on whether they think B is higher or lower.
    answer = input("\nWho has more followers? Type 'A' or 'B': ")
    # Check if they are right or wrong. User wins ties.
    # If right increase score. A becomes B and print the logo and new A.
    # Also show how many followers the new A has.
    # A is chosen.
    if answer == 'A':
        if a_fol >= b_fol:
            score += 1
        else: # B is bigger.
            correct = False

    else: # B is chosen.
        if a_fol <= b_fol:
            score += 1
        else: # A is bigger.
            correct = False
    # Only print A if they were right.
    if correct:
        os.system('clear')
        print (high_low)
        print (f"Correct! {contender_b["name"]} has {b_fol} followers. Your current score is {score}.")
        if score == 5:
            print ("You've made it quite far. Are you getting nervous?")
        elif score == 8:
            print ("Do you really think you have what it takes to win this?")
        elif score == 10:
            print ("You watch a lot of social media. Don't you?")
        contender_a = contender_b
        show_contender("A",contender_a) 

# If wrong we leave the loop, print out the score, and end the game.
print (f"Incorrect! Your score is {score}.")