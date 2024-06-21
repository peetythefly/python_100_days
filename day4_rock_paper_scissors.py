import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
# Get the random number from the user
user = int (input ("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
# Generate a random number to use for rock, paper, or scissors
comp = random.randint (0, 2)
# Print what each person chose
choice = [rock, paper, scissors]
print (f'''You chose:
{choice[user]}
''')
print (f'''
The computer chose:
{choice[comp]}
''')
# Check who wins and print it
# Start with a tie
if user == comp:
    print ("It's a tie! We both lose.")
# We rule out a tie so with each choice you either win or lose.
elif user == 0:
    if comp == 2:
        print ("Rock crushes scissors. You win!")
    else:
        print ("Paper covers rock. You lose!")
elif user == 1:
    if comp == 0:
        print ("Paper covers rock. You win!")
    else:
        print ("Scissors cuts paper. You lose!")
elif user == 2:
    if comp == 1:
        print ("Scissors cuts paper. You win!")
    else:
        print ("Rock crushes scissors. You lose!")
