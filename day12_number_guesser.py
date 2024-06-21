from art import numerical, thumb
import os
import random
logo = numerical

# Loop for continual playing.
keep_playing = True
while keep_playing:
    os.system('clear')
    # Create the number
    num = random.randint(1,100)
    # Greet the user
    print (logo)
    print("Welcome traveler! This is the art of Numerical Deduction where you guess a number between 1 and 100.")
    # Ask if easy or hard.
    mode = input("Would you like easy mode (10 guesses) or hard mode (5 guesses). Type 'easy' or 'hard': ")

    # Set num_guesses based on response
    if mode == 'easy':
        num_guesses = 10
    else: # If they don't say easy then hard mode it is.
        num_guesses = 5

    won = False
    # Start the loop that is based on num_guesses left.
    while num_guesses > 0 and not won: 
        # Give them a guess. Make sure it's an int.
        guess = int(input("What is your guess? "))
        # Return high, low or win based on the guess
        if guess > num:
            print("Incorrect. Too high!")
            num_guesses -= 1
        elif guess < num:
            print("Incorrect. Too low!")
            num_guesses -= 1
        else: # guess == num
            print("Correct. You win!")
            print (thumb)
            won = True
        if not won:
            print(f"You have {num_guesses} guesses left.")
    if not won:
        print(f"You lose. The number was {num}.")
    # See if they want to play again.
    again = input("Do you want to play again? 'y' or 'n': ")
    if again == 'n':
        keep_playing = False